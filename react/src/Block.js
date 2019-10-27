import React from 'react';

export default (props) => {
    const style = {
        left: `${props.block[0]}%`,
        top: `${props.block[1]}%`
    };
    return (
        <div className="game-piece" style={style}></div>

    )
}