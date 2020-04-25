import React from "react";
import {makeStyles} from '@material-ui/styles';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import RestoreIcon from '@material-ui/icons/Restore';
import FavoriteIcon from '@material-ui/icons/Favorite';
import LocationOnIcon from '@material-ui/icons/LocationOn';


const useStyles = makeStyles({
  root: {
    justifyContent: "center",

  },
});


const NavComponent = ({toggle}) => {
  const classes = useStyles();
  const [value, setValue] = React.useState(true);

  const changeView = (val) => {
    toggle(val)
  };

  return (
    <BottomNavigation
      value={value}
      onChange={(event, newValue) => {
        setValue(newValue);
      }}
      showLabels
      className={classes.root}
    >
      <BottomNavigationAction label="Self concentration manager" onClick={() => changeView(true)} icon={<RestoreIcon/>}/>
      <BottomNavigationAction label="Teacher dashboard" onClick={() => changeView(false)} icon={<FavoriteIcon/>}/>
    </BottomNavigation>
  )
};

export default NavComponent;