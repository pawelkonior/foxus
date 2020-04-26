import React, {useState, useEffect, useRef} from 'react';
import './App.css';
import {makeStyles} from '@material-ui/core/styles';
import WebcamComponent from "./components/Webcam";
import NavComponent from "./components/nav";
import ConcentrationChartComponent from "./components/concentrationChart";
import PlayerComponent from "./components/playerComponent";
import LinearProgress from '@material-ui/core/LinearProgress';


import logo from './logo.png'
import socket from 'socket.io-client';


const useStyles = makeStyles((theme) => ({
  main: {
    display: "flex"
  },
  root: {
    flexGrow: 1,
    background: '#424242'

  },
  control: {
    padding: theme.spacing(2),
  },
  audience: {
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
    alignContent: 'flex-start',
    flexWrap: "wrap",
    padding: "5px",
    paddingTop: "15px",
    boxSizing: "content-box",
    flexGrow: 3,
    width: "100%"
  },
  panel: {
    flexGrow: 1
  },
  speaker: {},
  bar: {
    width: "100%"
  },
  dark: {
    background: '#424242'
  },
  info: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },
  teacher: {
    display: "flex",
    width: "100%"
  }
}));

const data = [1];

const socket2 = socket();

function App() {
  const classes = useStyles();

  const [connect, setConnect] = useState(true);
  const [view, setView] = useState(false);

  useEffect(() => {
    socket2.on('connected', () => {
      setConnect(true)
    });
  }, []);

  return (
    <div className={classes.root}>
      <div style={{position: "absolute"}}>
        <img src={logo} alt="" style={{
          width: "145px",
          height: "auto",
          margin: "10px",
          borderRadius: "4px",
          boxShadow: "0px 0px 13px 7px rgba(82,80,80,1)"
        }}/>
      </div>

      {connect && !view &&
      <section className={classes.main}>
        <section className={classes.audience}>
          {data.map(e => {
            return (
              <PlayerComponent ws={socket2} status={0} idx={e} key={e}/>
            )
          })
          }
        </section>

        <section className={classes.panel}>
          {/*<ConcentrationChartComponent ws={socket2}/>*/}
          <WebcamComponent ws={socket2}/>
        </section>
      </section>
      }

      {connect && view &&
      <section className={classes.main}>
        <section className={classes.teacher}>
          <WebcamComponent ws={socket2}/>
          {/*<ConcentrationChartComponent ws={socket2}/>*/}
        </section>
      </section>

      }

      {connect &&
      <section className={classes.bar}>
        <NavComponent toggle={setView}/>
      </section>
      }
      {!connect &&
      <div>
        <LinearProgress/>

        <div className={classes.info}>

          <h1>Connecting...</h1>
        </div>
      </div>
      }


    </div>
  );
}

export default App;





//
//
//
//
//
//
// import React, {useEffect, useState} from 'react';
//
// import {createMuiTheme, makeStyles, ThemeProvider} from '@material-ui/core/styles';
// import {orange} from '@material-ui/core/colors';
// import LinearProgress from "@material-ui/core/LinearProgress";
//
// import socket from 'socket.io-client';
//
// // import CustomCheckbox from "./components/checkbox";
// // import CameraStream from "./components/CameraStream";
// import Dashboard from "./components/dashboard/Dashboard";
// import Camera from "./components/camera/Camera";
// import Nav from "./components/nav/Nav";
// import CanvasMask from "./components/canvas/Canvas";
//
// const theme = createMuiTheme({
//   status: {
//     danger: orange[500],
//   },
//   palette: {
//     primary: {
//       main: '#ff4400',
//     },
//     secondary: {
//       light: '#0066ff',
//       main: '#0044ff',
//       contrastText: '#ffcc00',
//     },
//     contrastThreshold: 3,
//     tonalOffset: 0.2,
//   },
//   typography: {
//     fontSize: "10px"
//   }
// });
//
// const useStyles = makeStyles((theme) => ({
//   main: {
//     position: "relative",
//     maxWidth: "850px",
//     width: "100%",
//     margin: "auto"
//   }
// }));
//
// const websocket = socket();
//
// function App() {
//   const classes = useStyles();
//
//   const [connect, setConnect] = useState(true);
//   const [view, setView] = useState(false);
//
//   useEffect(() => {
//     websocket.on('connected', () => {
//       setConnect(true)
//     });
//   }, []);
//
//   return (
//     <ThemeProvider theme={theme}>
//       <div className={classes.main}>
//         <LinearProgress/>
//         <Dashboard/>
//         <section className={classes.main}>
//           <section className={classes.teacher}>
//             <Camera ws={websocket}/>
//           </section>
//         </section>
//       </div>
//       {/*<CanvasMask></CanvasMask>*/}
//       <section className={classes.bar}>
//         <Nav toggle={setView}/>
//       </section>
//     </ThemeProvider>
//   );
// }
//
// export default App;
