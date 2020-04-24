import React, {useEffect, useState} from "react";
import Webcam from "react-webcam"

// const io = require('socket.io-client');
// const socket = io('http://localhost:3011');

const videoConstraints = {
  // width: 640,
  // height: 640,
  facingMode: "user"
};

const Camera = ({ws}) => {
  const webcamRef = React.useRef(null);

  const capture = React.useCallback(
    () => {
      const imageSrc = webcamRef.current.getScreenshot();
      if (imageSrc !== null){
        ws.emit('stream', {stream: imageSrc, id: 1});
      }
    },
    [webcamRef]
  );

  useEffect(() => {
    const interval = setInterval(() => {
      capture()
    }, 30);
    return () => clearInterval(interval);
  }, [capture]);

  return (
    <>
      <Webcam
        audio={false}
        // height={720}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
        videoConstraints={videoConstraints}
      />
    </>
  );
};

export default Camera