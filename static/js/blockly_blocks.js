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

const switchBlock = {
  "type": "block_dropdown",
  "message0": "Colour %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "drop_colour",
      "options": [
        [
          "is red",
          "R"
        ],
        [
          "is green",
          "G"
        ],
        [
          "is blue",
          "B"
        ]
      ]
    }
  ],
  "colour": 230,
  "tooltip": "Choose one of options"
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

  Blockly.Blocks['block_dropdown'] = {
    init: function () {
      this.jsonInit(switchBlock);
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

  Blockly.JavaScript['block_dropdown'] = function(block) {
    var dropdown_drop_colour = block.getFieldValue('drop_colour');
    let value = set_colour(dropdown_drop_colour);
    return `
            document.getElementById('console').innerText += ${value} + '\\n';
        `;

  };

};

const set_colour = (colour) => {
  const ret = '\'You selected colour of ' + colour + '\'';
  return ret;
}
