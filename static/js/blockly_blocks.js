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
  "tooltip": "Output the value",
  'colour': 120,
};

const inputBlock = {
  'type': 'input',
  'message0': 'input',
  'output': null,
  'tooltip': "Get the next value from the input",
  'colour': 120,
};

const additionBlock = {
  'type': 'math_addition',
  'message0': '%1 + %2',
  'args0': [
    {
      'type': 'input_value',
      'name': 'VALUE_1',
      'check': 'Number',
    },
    {
      'type': 'input_value',
      'name': 'VALUE_2',
      'check': 'Number',
    }
  ],
  'inputsInline': true,
  'output': 'Number',
  'colour': 210,
  'tooltip': 'Add the two numbers',
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

  Blockly.Blocks['math_addition'] = {
    init: function() {
      this.jsonInit(additionBlock);
    }
  };

  Blockly.JavaScript['output'] = (block) => {
      let value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
      return `
          (() => {
            toOutput = ${value}; 
            if (showOutput) {
              document.getElementById('outputs').innerText += '>>> ' + toOutput + '\\n';
            }
            outputArr.push(toOutput);
          })();
      `;
  };

  Blockly.JavaScript['input'] = (block) => {
    const code = `
      (() => {
        if (inputIdx < inputArr.length) {
          return inputArr[inputIdx++];
        }
        throw 'out of input';
      })()
    `;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.JavaScript['math_addition'] = (block) => {
    let value1 = Blockly.JavaScript.valueToCode(block, 'VALUE_1', Blockly.JavaScript.ORDER_ATOMIC);
    let value2 = Blockly.JavaScript.valueToCode(block, 'VALUE_2', Blockly.JavaScript.ORDER_ATOMIC);
    const code = `
     (${value1} + ${value2})
    `;
    return [code, Blockly.JavaScript.ORDER_ADDITION];

  }
};
