import React from "react";
import {makeStyles} from '@material-ui/core/styles';
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormGroup from "@material-ui/core/FormGroup";
import Switch from "@material-ui/core/Switch";
import DoneIcon from '@material-ui/icons/Done';
import BlockIcon from '@material-ui/icons/Block';
import {camelToText} from "../../helpers/helpers";

const useStyles = makeStyles((theme) => ({
  root: {
    color: theme.status.danger,
    '&$checked': {
      color: theme.status.danger,
    },
  },
  box: {
    background: "rgba(0, 0, 0, 0.5)",
    borderRadius: "10px",
    padding: "10px 10px 10px 20px",
    position: "absolute",
    right: "10px",
    top: "10px"
  },
  switchLabel: {
    fontSize: "10px"
  },
  formControlLabelText: {
    fontSize: '10px'
  }

}));

const data = [
  "upperJawlineLeft",
  "midJawlineLeft",
  "midJawlineRight",
  "chinBottom",
  "leftEyeBrowLeft",
  "leftEyeBrowUp",
  "leftEyeBrowRight",
  "leftEyeUp",
  "leftEyeRight",
  "leftEyeDown",
  "leftEyeLeft",
  "leftPupil",
  "upperJawlineRight",
  "rightEyeBrowLeft",
  "rightEyeBrowUp",
  "rightEyeBrowRight",
  "rightEyeUp",
  "rightEyeRight",
  "rightEyeDown",
  "rightEyeLeft",
  "rightPupil",
  "nose",
  "nodeLeft",
  "noseRight",
  "mouthLeft",
  "mouthRight",
  "mouthUp",
  "mouthDown"
];

function Dashboard() {
  const classes = useStyles();
  const [checked, setChecked] = React.useState(false);

  const toggleChecked = () => {
    setChecked((prev) => !prev);
  };

  return (
    <>
      <section className={classes.box}>
        <FormGroup>
          {data.map(item => {
            return (
              <div>
                <FormControlLabel
                  control={<Switch size="small" checked={checked} onChange={toggleChecked}/>}
                  label={camelToText(item)}
                  labelPlacement="end"
                  className={classes.formControlLabelText}
                />
                <DoneIcon/>
                <BlockIcon />
              </div>

            )
          })}
        </FormGroup>

      </section>
    </>
  );
}

export default Dashboard;