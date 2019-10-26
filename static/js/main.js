const Blockly = require('blockly');

const toolbox = `
  <xml id="toolbox" style="display: none">
	<block type="controls_if"></block>
	<block type="controls_repeat_ext"></block>
	<block type="logic_compare"></block>
	<block type="math_number"></block>
	<block type="math_arithmetic"></block>
	<block type="text"></block>
	<block type="text_print"></block>
  </xml>
`;

Blockly.inject('app', {toolbox});
