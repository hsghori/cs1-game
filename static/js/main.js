require('babel-polyfill');
const Blockly = require('blockly');
const $ = require('jquery');
const axios = require('axios');
const Cookies = require('js-cookie');
const modalInit = require('styledot/modal-init');
const { initBlocks } = require('./blockly_blocks');


const getToolbox = () => {
	const blocks = document.getElementById('app').dataset.blocks.split(', ');
	const variableIdx = blocks.findIndex((el) => el === 'variable');
	let extraCategories = '';
	if (variableIdx >= 0) {
		blocks.splice(variableIdx, 1);
		extraCategories = '<category name="Variables" colour="#a55b80" custom="VARIABLE"></category>';
	}
	const standardBlocks = blocks
		.map((block) => `<block type="${block}"></block>`)
		.reduce((prev, curr, idx) => prev + '\n' +  curr, '');
	if (extraCategories) {
		return `
			<xml id="toolbox">
				<category name="Basic Operations">
					${standardBlocks}
				</category>
				${extraCategories}
			</xml>
		`;
	} else {
		return `
			<xml id="toolbox">
				${standardBlocks}
			</xml>
		`;
	}
};

const setInput = () => {
	const inputArr = JSON.parse(document.getElementById('app').dataset.inputs);
	const inputString = inputArr.length
		? inputArr.join('\n')
		: 'None';
	$('#inputs').text(inputString);
	return inputArr;
};

const checkGame = async (game_pk, inputArr, outputArr) => {
	const csrftoken = Cookies.get('csrftoken');
	const response = await axios.post(
		`/api/check-game/${game_pk}/`,
		{'inputs': inputArr, 'outputs': outputArr},
		{headers: {'X-CSRFToken': csrftoken}}
	);
	const data = response.data;
	if (data.passed) {
		const modalContents = `
			<h3>Congrats!</h3>
			<p>Your solution passed!</p>
			<a class="sd-button" href="/">Next</a>
		`;
		modalInit.default({
			contents: modalContents,
		});
	} else {
		const modalContents = `
			<h3>Try again!</h3>
			<p>Your solution did not pass.</p>
		`;
		modalInit.default({
			contents: modalContents,
			dismissText: 'Try again!',
			ctaPosition: 'center',
			includeDismissCta: true,
		});
	}
};


$('document').ready(() => {
	initBlocks();
	const workspace = Blockly.inject('app', {toolbox: getToolbox()});
	const id = document.getElementById('app').dataset.id;
	const inputArr = setInput();
	const outputArr = [];
	$('#run').click(() => {
		window.LoopTrap = 1000;
		Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
		let code = Blockly.JavaScript.workspaceToCode(workspace);
		console.log(code);
		const inputIdx = 0;
		$('#outputs').text('');
		try {
			eval(code);
			checkGame(id, inputArr, outputArr);
		} catch (e) {
			alert('An error has occurred');
		}
	});
});
