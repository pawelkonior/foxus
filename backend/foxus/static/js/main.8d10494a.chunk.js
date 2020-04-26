(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{127:function(e,t){},130:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),c=n(14),o=n.n(c),i=(n(86),n(9)),l=(n(87),n(155)),s=n(70),u=n.n(s),f={facingMode:"user"},m=function(e){var t=e.ws,n=r.a.useRef(null),c=r.a.useCallback((function(){var e=n.current.getScreenshot();null!==e&&t.emit("stream",{stream:e,id:1})}),[n]);return Object(a.useEffect)((function(){var e=setInterval((function(){c()}),30);return function(){return clearInterval(e)}}),[c]),r.a.createElement(r.a.Fragment,null,r.a.createElement(u.a,{audio:!1,ref:n,screenshotFormat:"image/jpeg",width:320,videoConstraints:f}))},d=n(133),p=n(154),h=n(157),g=n(75),b=n.n(g),E=n(76),x=n.n(E),w=Object(d.a)({root:{justifyContent:"center"}}),v=function(e){var t=e.toggle,n=w(),a=r.a.useState(!0),c=Object(i.a)(a,2),o=c[0],l=c[1],s=function(e){t(e)};return r.a.createElement(p.a,{value:o,onChange:function(e,t){l(t)},showLabels:!0,className:n.root},r.a.createElement(h.a,{label:"Self concentration manager",onClick:function(){return s(!0)},icon:r.a.createElement(b.a,null)}),r.a.createElement(h.a,{label:"Teacher dashboard",onClick:function(){return s(!1)},icon:r.a.createElement(x.a,null)}))},j=n(43),O=n(42),y=!0,C=function(e){var t=e.ws,n=Object(a.useState)([]),c=Object(i.a)(n,2),o=c[0],l=c[1],s=Object(a.useState)([]),u=Object(i.a)(s,2),f=u[0],m=u[1];return Object(a.useEffect)((function(){t.on("chart stream",(function(e){var t=e.focus_mean[1];t[0]=new Date(e.focus_mean[1][0]).toLocaleTimeString(),y?(l((function(n){return[e.focus_mean[0],t]})),m((function(t){return e.focus_personally})),y=!1):(l((function(e){return e.length<=10?[].concat(Object(j.a)(e),[t]):[e[0]].concat(Object(j.a)(e.slice(-10)),[t])})),m((function(t){return e.focus_personally})))}))}),[t]),r.a.createElement(r.a.Fragment,null,r.a.createElement(O.a,{width:"100%",height:"300px",chartType:"LineChart",loader:r.a.createElement("div",null,"Loading Chart"),data:o,colors:["red"],curveType:"function",legend:{position:"bottom"},options:{title:"Mean focus"},rootProps:{"data-testid":"1"}}),r.a.createElement(O.a,{width:"100%",height:"300px",chartType:"ColumnChart",loader:r.a.createElement("div",null,"Loading Chart"),data:f,options:{chartArea:{width:"80%",height:"70%"}},rootProps:{"data-testid":"1"}}))};n(92);var S=function(e){var t=e.idx,n=e.status,c=e.ws,o=Object(a.useRef)(null),l=Object(a.useState)(n),s=Object(i.a)(l,2),u=s[0],f=s[1];return Object(a.useEffect)((function(){c.on("stream processed",(function(e){o.current.src=e}))}),[c]),Object(a.useEffect)((function(){c.on("user processed",(function(e){e.idx===t&&f(e.status)}))}),[c]),r.a.createElement("div",{style:{width:"320px",height:"240px",boxSizing:"border-box",boxShadow:"0px 0px 5px 3px"+["#ffffff","#00ff09","#ff0000","#000dff"][u],marginBottom:"15px",marginRight:"15px",zIndex:10,position:"relative"}},r.a.createElement("img",{src:"",alt:"",ref:o}))},k=n(158),N=n(78),I=n.n(N),T=n(79),L=n.n(T),_=Object(l.a)((function(e){return{main:{display:"flex"},root:{flexGrow:1,background:"#424242"},control:{padding:e.spacing(2)},audience:{display:"flex",justifyContent:"center",alignItems:"flex-start",alignContent:"flex-start",flexWrap:"wrap",padding:"5px",paddingTop:"15px",boxSizing:"content-box",flexGrow:3,width:"100%"},panel:{flexGrow:1},speaker:{},bar:{width:"100%"},dark:{background:"#424242"},info:{display:"flex",alignItems:"center",justifyContent:"center"},teacher:{display:"flex",width:"100%"}}})),R=[1,2,3,4],z=L()();var B=function(){var e=_(),t=Object(a.useState)(!0),n=Object(i.a)(t,2),c=n[0],o=n[1],l=Object(a.useState)(!1),s=Object(i.a)(l,2),u=s[0],f=s[1];return Object(a.useEffect)((function(){z.on("connected",(function(){o(!0)}))}),[]),r.a.createElement("div",{className:e.root},r.a.createElement("div",{style:{position:"absolute"}},r.a.createElement("img",{src:I.a,alt:"",style:{width:"50px",height:"auto",margin:"10px",borderRadius:"4px",boxShadow:"0px 0px 13px 7px rgba(82,80,80,1)"}})),c&&!u&&r.a.createElement("section",{className:e.main},r.a.createElement("section",{className:e.audience},R.map((function(e){return r.a.createElement(S,{ws:z,status:0,idx:e,key:e})}))),r.a.createElement("section",{className:e.panel},r.a.createElement(C,{ws:z}),r.a.createElement(m,{ws:z}))),c&&u&&r.a.createElement("section",{className:e.main},r.a.createElement("section",{className:e.teacher},r.a.createElement(m,{ws:z}),r.a.createElement(C,{ws:z}))),c&&r.a.createElement("section",{className:e.bar},r.a.createElement(v,{toggle:f})),!c&&r.a.createElement("div",null,r.a.createElement(k.a,null),r.a.createElement("div",{className:e.info},r.a.createElement("h1",null,"Connecting..."))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var F=n(156),G=n(80),M=Object(G.a)({palette:{type:"dark"}});o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(F.a,{theme:M},r.a.createElement(B,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},78:function(e,t,n){e.exports=n.p+"static/media/logo.70f37bca.png"},81:function(e,t,n){e.exports=n(130)},86:function(e,t,n){},87:function(e,t,n){}},[[81,1,2]]]);
//# sourceMappingURL=main.8d10494a.chunk.js.map