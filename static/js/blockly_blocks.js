const Blockly = require('blockly');

const outputBlock = {
  "type": "output",
  "message0": "output %1",
  "args0": [
    {
      "type": "input_value",
      "name": "VALUE"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "tooltip": "Put the value in the final output",
};


export const initBlocks = () => {
  Blockly.Blocks['output']  = {
	init: function() {
		this.jsonInit(outputBlock);
	}
  };

  Blockly.JavaScript['output'] = function(block) {
      let value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
      return `
          document.getElementById('console').innerText += ${value} + '\\n';
      `;
  };
};
