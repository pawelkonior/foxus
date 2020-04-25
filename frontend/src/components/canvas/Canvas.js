import React from "react";

const HOOK_SVG = "M948.6,367.7v162.1l34.1,34.1L911.6,638l-72-71.9l49.3-44.9v-128C679.5,479.6,612.4,506.4,566,527.4s-79.9,20.8-125.9,3.5c-46-17.4-265.2-97.3-374.1-149.4c-72.6-34.8-77.3-56.8,1.2-86.3c102.5-38.9,271.9-101.3,361.7-135.3c53.2-21.5,81.3-33.2,130.1-8.7c87.1,36,286.2,110.7,385.2,151.6C1030.5,340.3,972.6,352.6,948.6,367.7L948.6,367.7z M576.1,591.6c50.6-20.9,118.9-55.4,193.3-87.3v256c0,0-96.2,102.4-265.4,102.4c-182.2,0-280.6-102.4-280.6-102.4V521.3c57.4,23.4,121.9,43.5,200,70.3C471.4,608.7,532.5,614.6,576.1,591.6L576.1,591.6z"
const HOOK_PATH = new Path2D(HOOK_SVG)
const SCALE = 0.3
const OFFSET = 80

var vertices=[];
vertices.push({x:0,y:0});
vertices.push({x:300,y:100});
vertices.push({x:80,y:200});
vertices.push({x:10,y:100});
vertices.push({x:0,y:0});

// calc waypoints traveling along vertices
function calcWaypoints(vertices){
  var waypoints=[];
  for(var i=1;i<vertices.length;i++){
    var pt0=vertices[i-1];
    var pt1=vertices[i];
    var dx=pt1.x-pt0.x;
    var dy=pt1.y-pt0.y;
    for(var j=0;j<100;j++){
      var x=pt0.x+dx*j/100;
      var y=pt0.y+dy*j/100;
      waypoints.push({x:x,y:y});
    }
  }
  return(waypoints);
}


function draw(ctx, location) {
  ctx.fillStyle = 'deepskyblue'
  ctx.shadowColor = 'dodgerblue'
  // ctx.shadowBlur = 20
  ctx.fillRect(10,10,100,100);
  var circle = new Path2D();
  circle.moveTo(125, 35);
  circle.arc(200, 35, 25, 0, 2 * Math.PI);
  ctx.fill(circle);
  var startX = 50;
  var startY = 50;
  var endX = 100;
  var endY = 100;
  var amount = 0;
  setInterval(function() {
    amount += 0.05;
    ctx.clearRect(0, 0, 500, 500);
    ctx.strokeStyle = "red";
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX + (endX - startX) * amount, startY + (endY - startY) * amount + -100 *amount);
    ctx.stroke();
  }, 30);
  ctx.save()
  ctx.scale(SCALE, SCALE)
  ctx.translate(location.x / SCALE - OFFSET, location.y / SCALE - OFFSET)
  // ctx.fill(HOOK_PATH)
  ctx.restore()
}

const CanvasMask = () => {
  const [locations, setLocations] = React.useState(
    JSON.parse(localStorage.getItem('draw-app')) || []  )
  const canvasRef = React.useRef(null)
  React.useEffect(() => {
    const canvas = canvasRef.current
    const ctx = canvas.getContext('2d')
    ctx.clearRect(0, 0, window.innerHeight, window.innerWidth)
    locations.forEach(location => draw(ctx, location))
  })
  React.useEffect(() => {
    localStorage.setItem('draw-app', JSON.stringify(locations))
  })
  function handleCanvasClick(e) {
    const newLocation = { x: e.clientX, y: e.clientY }
    setLocations([...locations, newLocation])
  }
  function handleClear() {
    setLocations([])
  }
  function handleUndo() {
    setLocations(locations.slice(0, -1))
  }
  return (
    <>
      <div className="controls">
        <button onClick={handleClear}>Clear</button>
        <button onClick={handleUndo}>Undo</button>
      </div>
      <canvas
        ref={canvasRef}
        width={window.innerWidth}
        height={window.innerHeight}
        onClick={handleCanvasClick}
      />
    </>
  )
};

export default CanvasMask;