import React, {useEffect, useState} from "react";
import Chart from "react-google-charts"

let counter = true;

const data = [
  ["Name", "Focus", {role: 'style'}],
  ["Kasia", 95, "blue"],
  ["Wojtek", 32, "red"],
  ["Piotrek", 51, "green"],
  ["Marcin", 75, "grey"],
  ["Pawel", 80, "orange"],
  ["Radek", 62, "yellow"]
];

const data1 = [
  ["Time", "Val"],
  ["04:42:45", 20],
  ["04:42:46", 30],
  ["04:42:47", 40],
  ["04:42:48", 50],
  ["04:42:49", 60],
  ["04:42:50", 70],
  ["04:42:51", 70],
  ["04:42:52", 100],
];


const ConcentrationChartComponent = ({ws}) => {

  const [dataChartMean, setDataChartMean] = useState([]);
  const [dataChartIndMean, setDataChartIndMean] = useState([]);

  useEffect(() => {
    ws.on('chart stream', payload => {
      const newData = payload.focus_mean[1];
      newData[0] = new Date(payload.focus_mean[1][0]).toLocaleTimeString();
      if (counter) {
        setDataChartMean(old => [payload.focus_mean[0], newData]);
        setDataChartIndMean(old => payload.focus_personally);
        counter = false;
      } else {
        setDataChartMean(old => old.length <= 10 ? [...old, newData] : [old[0], ...(old).slice(-10), newData]);
        setDataChartIndMean(old => payload.focus_personally);
      }
    });
  }, [ws]);

  return (
    <>
      <Chart
        width={'100%'}
        height={'300px'}
        chartType="LineChart"
        loader={<div>Loading Chart</div>}
        data={dataChartMean}
        colors={['red']}
        curveType='function'
        legend={{position: 'bottom'}}
        options={{
          title: 'Mean focus',
          // hAxis: {
          //   titleTextStyle: {color: '#607d8b'},
          //   textStyle: { color: '#b0bec5', fontName: 'Roboto', fontSize: '12', bold: true}
          // },
          // vAxis: {
          //   minValue: 0,
          //   baselineColor: 'transparent'
          // },
          // legend: {position: 'top', alignment: 'center', textStyle: {color:'#607d8b', fontName: 'Roboto', fontSize: '12'} },
          // colors: ["#3f51b5","#2196f3","#03a9f4","#00bcd4","#009688","#4caf50","#8bc34a","#cddc39"],
          // areaOpacity: 0.24,
          // lineWidth: 1,
          // chartArea: {
          //   backgroundColor: "transparent",
          //   width: '100%',
          //   height: '80%'
          // },
          // height: "300px", // example height, to make the demo charts equal size
          // width: "100%",
          // pieSliceBorderColor: '#263238',
          // pieSliceTextStyle:  {color:'#607d8b' },
          // pieHole: 0.9,
          // bar: {groupWidth: "40" },
          // colorAxis: {colors: ["#3f51b5","#2196f3","#03a9f4","#00bcd4"] },
          // backgroundColor: 'transparent',
          // datalessRegionColor: '#37474f',
          // displayMode: 'regions'

          // lineWidth: 25
        }}
        // For tests
        rootProps={{'data-testid': '1'}}
      />

      <Chart
        width={'100%'}
        height={'300px'}
        chartType="ColumnChart"
        loader={<div>Loading Chart</div>}
        data={dataChartIndMean}
        options={{
          chartArea: {width: '80%', height: '70%'},
          // lineWidth: 25
        }}
        // For tests
        rootProps={{'data-testid': '1'}}
      />
    </>
  )
};

export default ConcentrationChartComponent