import React, {useEffect, useRef, useState} from "react";
// import ReactPlayer from "react-player";

const PlayerComponent = ({idx, status, ws}) => {
  const player = useRef(null);
  const colors = ["#ffffff", "#00ff09", "#ff0000", "#000dff"];

  const [color, setColor] = useState(status);

  useEffect(() => {
    ws.on('stream processed', payload => {
      player.current.src = payload
    });
  }, [ws]);

  useEffect(() => {
    ws.on('user processed', payload => {
      if (payload.idx === idx) {
        setColor(payload.status)
      }
    });
  }, [ws]);

  return (
    <div style={{
      width: "640px",
      // maxWidth: "40%",
      height: "480px",
      // maxHeight: "200px",
      boxSizing: "border-box",
      boxShadow: "0px 0px 5px 3px" + colors[color],
      marginBottom: "15px",
      marginRight: "15px",
      zIndex: 10,
      position: "relative"
    }}>
      <img src="" alt="" ref={player} style={{width: '100%', height: '100%'}}/>
    </div>
  )
};

export default PlayerComponent;