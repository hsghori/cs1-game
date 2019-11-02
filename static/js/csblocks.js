/**
 * CS Professor : sample
 * [1] Walk through the steps of defining blocks
 * https://developers.google.com/blockly/guides/create-custom-blocks/blockly-developer-tools
 * 
 * [2] Blockly Developer Tools (2nd item from the bottom)
 * https://blockly-demo.appspot.com/static/demos/blockfactory/index.html
 * 
 */

// 1) definition
Blockly.Blocks['lightswitch'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn")
        .appendField(new Blockly.FieldDropdown([["red","R"], ["yellow","Y"], ["orange","O"], ["all","all"]]), "lightcolor")
        .appendField(new Blockly.FieldDropdown([["on","on"], ["off","off"]]), "switch");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(90);
 this.setTooltip("5");
 this.setHelpUrl("");
  }
};



// 2) generator stub
Blockly.JavaScript['lightswitch'] = function(block) {
  var dropdown_lightcolor = block.getFieldValue('lightcolor');
  var dropdown_switch = block.getFieldValue('switch');

  // TODO: Assemble JavaScript into code variable.
  // Below is the piece of code implementated.
  var code = '...;\n';
  if(dropdown_switch ==="on"){
      var code = "document.getElementById('square').style.backgroundColor='red';\n"
  }
  if(dropdown_switch ==="off"){
      var code = "document.getElementById('square').style.backgroundColor='white';\n"        
  }
  return code;
};