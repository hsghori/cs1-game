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
	const conditionIdx = blocks.findIndex((el) => el === 'condition');
	let extraCategories = '';

	if (conditionIdx >= 0) {
		blocks.splice(conditionIdx, 1);
		extraCategories += `<category name="Condition (if-else)" colour="#a55b80">
		<block type="controls_if"></block>
		<block type="controls_if"><mutation else="1"></mutation></block>
		<block type="controls_if"><mutation elseif="1" else="1"></mutation></block>
		</category>
		`;
	}
	if (variableIdx >= 0) {
		blocks.splice(variableIdx, 1);
		extraCategories += '<category name="Variables" colour="#a55b80" custom="VARIABLE"></category>';
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

const workspaceOptions = {
	toolbox: getToolbox(),
	collapse: false,
	comments: false,
	disable: false,
	maxBlocks: Infinity,
	trashcan: true,
	horizontalLayout: false,
	toolboxPosition: 'start',
	css: true,
	media: 'https://blockly-demo.appspot.com/static/media/',
	sounds: true,
	oneBasedIndex: true
};

const setInput = () => {
	const inputArr = JSON.parse(document.getElementById('app').dataset.inputs);
	document.getElementById('inputs').innerHTML = inputArr.length
		? inputArr.join('<br>')
		: 'None';
	return inputArr;
};

const checkGame = async (game_pk, inputArr, outputArr) => {
	const csrftoken = Cookies.get('csrftoken');
	const response = await axios.post(
		`/api/check-game/${game_pk}/`,
		{inputs: inputArr, outputs: outputArr},
		{headers: {'X-CSRFToken': csrftoken}}
	);
	const data = response.data;
	if (data.passed) {
		const nextLink = data.next_game
			? `/game/${data.next_game}/`
			: '/';
		const modalContents = `
			<h3>Good work!</h3>
			<p>Your solution passed!</p>
			<div style="display: flex; flex-direction: row; justify-content: space-around">
				<a class="sd-button" href="${nextLink}">Next</a>
			</div>
		`;
		modalInit.default({
			contents: modalContents,
			includeDismissCta: false,
		});
	} else {
		const modalContents = `
			<h3>Try again!</h3>
			<p>Your solution did not match the expected output.</p>
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
	const workspace = Blockly.inject('app', workspaceOptions);
	const id = document.getElementById('app').dataset.id;
	const inputArr = setInput();
	
	$('#run').click(() => {
		window.LoopTrap = 1000;
		Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
		let code = Blockly.JavaScript.workspaceToCode(workspace);
		console.log(code);
		const outputArr = [];
		const inputIdx = 0;
		let toOutput = null;
		$('#outputs').text('');
		try {
			eval(code);
			checkGame(id, inputArr, outputArr);
		} catch (e) {
			const modalContents = `
				<h3>Whoops</h3>
				<p>Your solution failed with an error.</p>
				<p>${e}</p>
			`;
			modalInit.default({
				contents: modalContents,
				dismissText: 'Try again!',
				ctaPosition: 'center',
				includeDismissCta: true,
			});
		}
	});
});
