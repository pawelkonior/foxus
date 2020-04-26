import React, {useEffect, useRef, useState} from "react";
// import ReactPlayer from "react-player";

function encode (input) {
  var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var output = "";
  var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
  var i = 0;

  while (i < input.length) {
    chr1 = input[i++];
    chr2 = i < input.length ? input[i++] : Number.NaN; // Not sure if the index
    chr3 = i < input.length ? input[i++] : Number.NaN; // checks are needed here

    enc1 = chr1 >> 2;
    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
    enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
    enc4 = chr3 & 63;

    if (isNaN(chr2)) {
      enc3 = enc4 = 64;
    } else if (isNaN(chr3)) {
      enc4 = 64;
    }
    output += keyStr.charAt(enc1) + keyStr.charAt(enc2) +
      keyStr.charAt(enc3) + keyStr.charAt(enc4);
  }
  return output;
}

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
      <img src="" alt="" ref={player}/>
    </div>
  )
};

export default PlayerComponent;