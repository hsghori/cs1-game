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
	const inputArr = JSON.parse(document.getElementById('app').dataset.inputs1);
	document.getElementById('inputs').innerHTML = inputArr.length
		? inputArr.join('<br>')
		: 'None';
	return inputArr;
};


const checkGame = (gamePk, inputs, outputs) => {
	const csrftoken = Cookies.get('csrftoken');
	axios.post(
		`/api/check-game/${gamePk}/`,
		{inputs, outputs},
		{headers: {'X-CSRFToken': csrftoken}}
	).then((response) => {
		const { passed, next_game: nextGamePk } = response.data;
		if (passed) {
			const nextLink = nextGamePk ? `/game/${nextGamePk}/` : '/';
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
	}).catch((err) => {
		const modalContents = `
			<h3>Whoops</h3>
			<p>An error occurred.</p>
			<p>Please try again later.</p>
		`;
		modalInit.default({
			contents: modalContents,
			dismissText: 'Try again!',
			ctaPosition: 'center',
			includeDismissCta: true,
		});
	});
};


const runCode = (code, inputArr, showOutput = false) => {
	const outputArr = [];
	let toOutput = null;
	let inputIdx = 0;
	eval(code);
	return outputArr;
};


$('document').ready(() => {
	initBlocks();
	const workspace = Blockly.inject('app', {toolbox: getToolbox()});

	// keep the category open after placing a block
	workspace.toolbox_.flyout_.autoClose = false;
	const gamePk = document.getElementById('app').dataset.id;

	const inputs = [
		setInput(),
		JSON.parse(document.getElementById('app').dataset.inputs2),
		JSON.parse(document.getElementById('app').dataset.inputs3),
	];
	
	$('#run').click(() => {
		window.LoopTrap = 1000;
		Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
		let code = Blockly.JavaScript.workspaceToCode(workspace);
		$('#outputs').text('');
		try {
			const outputs = inputs.map((arr, idx) => {
				return runCode(code, arr, idx === 0);
			});
			checkGame(gamePk, inputs, outputs);
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
