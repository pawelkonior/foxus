import React, {useEffect, useState} from 'react';

import {createMuiTheme, makeStyles, ThemeProvider} from '@material-ui/core/styles';
import {orange} from '@material-ui/core/colors';
import LinearProgress from "@material-ui/core/LinearProgress";

import socket from 'socket.io-client';

// import CustomCheckbox from "./components/checkbox";
// import CameraStream from "./components/CameraStream";
import Dashboard from "./components/dashboard/Dashboard";
import Camera from "./components/camera/Camera";
import Nav from "./components/nav/Nav";
import CanvasMask from "./components/canvas/Canvas";

const theme = createMuiTheme({
  status: {
    danger: orange[500],
  },
  palette: {
    primary: {
      main: '#ff4400',
    },
    secondary: {
      light: '#0066ff',
      main: '#0044ff',
      contrastText: '#ffcc00',
    },
    contrastThreshold: 3,
    tonalOffset: 0.2,
  },
  typography: {
    fontSize: "10px"
  }
});

const useStyles = makeStyles((theme) => ({
  main: {
    position: "relative",
    maxWidth: "850px",
    width: "100%",
    margin: "auto"
  }
}));

const websocket = socket();

function App() {
  const classes = useStyles();

  const [connect, setConnect] = useState(true);
  const [view, setView] = useState(false);

  useEffect(() => {
    websocket.on('connected', () => {
      setConnect(true)
    });
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <div className={classes.main}>
        <LinearProgress/>
        <Dashboard/>
        <section className={classes.main}>
          <section className={classes.teacher}>
            <Camera ws={websocket}/>
          </section>
        </section>
      </div>
      <CanvasMask></CanvasMask>
      <section className={classes.bar}>
        <Nav toggle={setView}/>
      </section>
    </ThemeProvider>
  );
}

export default App;
