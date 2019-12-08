require('babel-polyfill');
const Blockly = require('blockly');
const $ = require('jquery');
const axios = require('axios');
const Cookies = require('js-cookie');
const modalInit = require('styledot/modal-init');
const { initBlocks } = require('./blockly_blocks');


String.prototype.toProperCase = function() {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};


const getToolbox = () => {
	const blocks = document.getElementById('app').dataset.blocks.split(', ');
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
	const variableIdx = blocks.findIndex((el) => el === 'variable');
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
		const { passed, next_game: nextGamePk, badges_awarded: badges } = response.data;
		if (passed) {
			const nextLink = nextGamePk ? `/game/${nextGamePk}/` : '/';
			let badgesStr = '';
			if (badges.length > 0) {
				badgesStr = `You\'ve earned the following badge(s):<br>\n<ul>`;
				badges.forEach((badge) => {
					badgesStr += `<li style="display: flex; flex-direction: row; align-items: center; ">
						<div style="margin-right: 8px;">${badge.slug.toProperCase()} - ${badge.name}</div>
						<img src="/static/img/shield.svg" style="height: 24px;"/>
					</li>`;
				});
				badgesStr += '</ul>';
				badgesStr += `
					<div style="display: flex; flex-direction: row; justify-content: space-around; margin-top: 8px; margin-bottom: 8px">
						<a class="sd-button" href="/badges/">View awards</a>
					</div>
				`;
			}

			const modalContents = `
				<h3>Good work!</h3>
				<p>Your solution passed!</p>
				<div>${badgesStr}</div>
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
			<p>${err}</p>
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
	const workspace = Blockly.inject('app', workspaceOptions);
	const gamePk = document.getElementById('app').dataset.id;

	const inputs = [
		setInput(),
		JSON.parse(document.getElementById('app').dataset.inputs2),
		JSON.parse(document.getElementById('app').dataset.inputs3),
	];

	$('#run').click(() => {
		// run the code on the example input but don't check it.
		window.LoopTrap = 1000;
		Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
		let code = Blockly.JavaScript.workspaceToCode(workspace);
		$('#outputs').text('');
		try {
			runCode(code, inputs[0], true);
		} catch (e) {
			const modalContents = `
				<h3>Whoops</h3>
				<p>Your code caused an error.</p>
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
	
	$('#run-and-submit').click(() => {
		// run the code on all inputs and check for correctness
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
