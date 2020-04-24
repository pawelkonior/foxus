import React from 'react';

import {createMuiTheme, makeStyles, ThemeProvider} from '@material-ui/core/styles';
import {orange} from '@material-ui/core/colors';
import LinearProgress from "@material-ui/core/LinearProgress";

// import CustomCheckbox from "./components/checkbox";
// import CameraStream from "./components/CameraStream";
// import Dashboard from "./components/Dashboard";

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


function App() {
  const classes = useStyles();

  return (
    <ThemeProvider theme={theme}>
      <div className={classes.main}>
        <LinearProgress/>
        <h1>Foqs</h1>
      </div>
    </ThemeProvider>
  );
}

export default App;
