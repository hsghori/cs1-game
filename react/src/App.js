import React, { Component } from 'react';
import Block from './Block'

// constant function and block size
const getRandomPosition = () => {
   let min = 1, max = 80;
   let x = Math.floor((Math.random() * (max - min + 1) + min) / 2) * 2;
   let y = Math.floor((Math.random() * (max - min + 1) + min) / 2) * 2;
   // return [x, y]
   return [0, 0]
}
const BLOCK_SIZE = 1

// main method
class App extends Component {
   state = {
      gameBlock: getRandomPosition(),
      speed: 200,
      direction: 'CENTER'
   }

   componentDidMount() {
      setInterval(this.moveBlock, this.state.speed);
      document.onkeydown = this.handleKeyDown;
   }

   handleKeyDown = (e) => {
      e = e || window.event;
      // console.log("(debug)",e.keyCode)
      switch (e.keyCode) {
         case 37:
            this.setState({ direction: 'WEST' });
            break;
         case 38:
            this.setState({ direction: 'NORTH' });
            break;
         case 39:
            this.setState({ direction: 'EAST' });
            break;
         case 40:
            this.setState({ direction: 'SOUTH' });
            break;
         default:
            break;
      }
   }


   moveBlock = () => {
      let block = this.state.gameBlock;
      let head = block;
      let x = block[0];
      let y = block[1];
      // console.log(head,", (x,y)=[",x,",",y , "]:", this.state.direction)
      switch (this.state.direction) {
         case 'WEST':
            head = [x - BLOCK_SIZE, y]
            break;
         case 'EAST':
            head = [x + BLOCK_SIZE, y]
            break;
         case 'NORTH':
            head = [x, y - BLOCK_SIZE]
            break;
         case 'SOUTH':
            head = [x, y + BLOCK_SIZE]
            break;
         default:
            break;
      }

      this.setState({
         gameBlock: head
      })

   }


   render() {
      return (
         <div className="blockly-area">
            <Block block={this.state.gameBlock} />
         </div>
      );
   }
}
export default App;