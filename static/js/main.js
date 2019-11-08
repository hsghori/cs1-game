const Blockly = require('blockly');
const $ = require('jquery');
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


$('document').ready(() => {
	initBlocks();
	const workspace = Blockly.inject('app', {toolbox: getToolbox()});
	$('#run').click(() => {
		window.LoopTrap = 1000;
		Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
		let code = Blockly.JavaScript.workspaceToCode(workspace);
		console.log(code);
		$('#console').text('');
		try {
			eval(code);
		} catch (e) {
			alert('An error has occurred');
		}
	});
});
