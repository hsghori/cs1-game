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

const inputBlock = {
  'type': 'input',
  'message0': 'input',
  'output': null,
  'tooltip': "Put the value in the final output",
};


export const initBlocks = () => {
  Blockly.Blocks['output']  = {
	init: function() {
		this.jsonInit(outputBlock);
	}
  };

  Blockly.Blocks['input'] = {
    init: function() {
      this.jsonInit(inputBlock);
    }
  };

  Blockly.JavaScript['output'] = (block) => {
      let value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
      return `
          document.getElementById('outputs').innerText += '>>> ' + ${value} + '\\n';
          outputArr.push(${value});
      `;
  };

  Blockly.JavaScript['input'] = (block) => {
    return ['inputArr[inputIdx++]', Blockly.JavaScript.ORDER_ATOMIC];
  };
};
