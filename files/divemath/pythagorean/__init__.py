from divewidgets import JSXGraph

discover_jxg = JSXGraph(code=r"""JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-1, 17, 17, -3], axis:true,grid:true, keepaspectratio:true,  showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 4, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});

var s = board.create('point', [6,6],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: true, size:2, name:'A', label:{offset:[-10,10]}});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: true, size:2, name:'C', label:{offset:[-10,-10]}});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: true, size:2, name:'B', label:{offset:[10,0]}});
var po1 = board.create('polygon',[tri1[0], tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});


var po_a = board.create('regularpolygon',[tri1[1],tri1[0],4], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var po_b = board.create('regularpolygon',[tri1[2],tri1[1],4], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var po_c = board.create('regularpolygon',[tri1[0],tri1[2],4], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});


board.create('text',[()=>s.X()+a.Value()/2,()=>s.Y()-a.Value()/2,function(){
        return (po_b.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()-b.Value()/2,()=>s.Y()+b.Value()/2,function(){
        return (po_a.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});
    
board.create('text',[()=>s.X()+a.Value(),()=>s.Y()+b.Value(),function(){
        return (po_c.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});
""", width=600, height=600, id="jxgbox")

proof1_jxg = JSXGraph(code=r"""JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-1, 13, 15, -3], axis:true, keepaspectratio:true,  showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 6, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});
var m = board.create('slider', [[1, -2], [12,-2], [0, 0, 2]], {name:'move', snapWidth: 0.1, withLabel:false});
board.create('text',[1+m.point2.X(),m.point2.Y(),"move"],{fixed: true, anchorX: 'middle'});
var s = board.create('point', [1,1],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var r2 = board.create('point', [s,right_ab], {visible: false});
var po0 =  board.create('regularpolygon',[s,r2,4], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: false});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: false});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: false});
var po1 = board.create('polygon',[tri1[0],tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});

var move_tri2 = board.create('transform', [()=>a.Value(), ()=>b.Value()*(1-Math.min(m.Value(),1))], {type:'translate'});
var tri2 = [];
tri2[0] = board.create('point', [s, move_tri2], {visible: false});
tri2[1] = board.create('point', [tri2[0], right_b], {visible: false});
tri2[2] = board.create('point', [tri2[0], [right_b,up_a]], {visible: false});
var po2 = board.create('polygon',[tri2[0],tri2[1],tri2[2]], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var move_tri3 = board.create('transform', [()=>a.Value()+b.Value()*(Math.max(m.Value(),1)-1), ()=>a.Value()*(Math.max(m.Value(),1)-1)], {type:'translate'});
var tri3 = [];
tri3[0] = board.create('point', [s, move_tri3], {visible: false});
tri3[1] = board.create('point', [tri3[0], up_b], {visible: false});
tri3[2] = board.create('point', [tri3[0], [up_b,left_a]], {visible: false});
var po3 = board.create('polygon',[tri3[0],tri3[1],tri3[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});


var move_tri4 = board.create('transform', [()=>b.Value()+a.Value()*(1-Math.min(m.Value(),1)), ()=>a.Value()+b.Value()], {type:'translate'});
var tri4 = [];
tri4[0] = board.create('point', [s, move_tri4], {visible: false});
tri4[1] = board.create('point', [tri4[0], left_b], {visible: false});
tri4[2] = board.create('point', [tri4[0], [left_b,down_a]], {visible: false});
var po4 = board.create('polygon',[tri4[0],tri4[1],tri4[2]], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('text',[()=>s.X()+1/2*a.Value(),()=>s.Y()+b.Value()+1/2*a.Value(),function(){
        return '\\[ a^2 \\]';
    }],{visible: ()=> {return (m.Value()<0.3);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+a.Value()+1/2*b.Value(),()=>s.Y()+1/2*b.Value(),function(){
    return '\\[b^2\\]';
    }],{visible: ()=> {return (m.Value()<0.3);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+1/2*(a.Value()+b.Value()),()=>s.Y()+1/2*(a.Value()+b.Value()),function(){
    return '\\[c^2\\]';
    }],{visible: ()=> {return (m.Value()>1.9);}, anchorX: 'middle', anchorY: 'auto'});
""", width=600, height=600, id="jxgbox")

proof2_jxg = JSXGraph(code=r"""JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-1, 13, 15, -3], axis:true, keepaspectratio:true,  showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 6, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});
var m = board.create('slider', [[1, -2], [12,-2], [0, 0, 2]], {name:'move', snapWidth: 0.1, withLabel:false});
board.create('text',[1+m.point2.X(),m.point2.Y(),"move"],{fixed: true, anchorX: 'middle'});
var s = board.create('point', [1,1],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var r2 = board.create('point', [s,right_ab], {visible: false});
var po0 =  board.create('regularpolygon',[s,r2,4], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: false});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: false});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: false});
var po1 = board.create('polygon',[tri1[0],tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});

var move_tri2 = board.create('transform', [()=>a.Value(), 0], {type:'translate'});
var tri2 = [];
tri2[0] = board.create('point', [s, move_tri2], {visible: false});
tri2[1] = board.create('point', [tri2[0], right_b], {visible: false});
tri2[2] = board.create('point', [tri2[0], [right_b,up_a]], {visible: false});
var po2 = board.create('polygon',[tri2[0],tri2[1],tri2[2]], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

//anchor of tri3 should be changed
/*
var move_tri3 = board.create('transform', [()=>a.Value()+b.Value(), ()=>a.Value()], {type:'translate'});
var tri3 = [];
tri3[0] = board.create('point', [s, move_tri3], {visible: false});
tri3[1] = board.create('point', [tri3[0], up_b], {visible: false});
tri3[2] = board.create('point', [tri3[0], [up_b,left_a]], {visible: false});
var po3 = board.create('polygon',[tri3[0],tri3[1],tri3[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});
*/

var move_tri3_2 = board.create('transform', [()=>b.Value(), ()=>a.Value()+b.Value()], {type:'translate'});
var tri3_2 = [];
tri3_2[0] = board.create('point', [s, move_tri3_2], {visible: false});
tri3_2[1] = board.create('point', [tri3_2[0], right_a], {visible: false});
tri3_2[2] = board.create('point', [tri3_2[0], [right_a, down_b]], {visible: false});
var po3 = board.create('polygon',[tri3_2[0],tri3_2[1],tri3_2[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var move_tri4 = board.create('transform', [()=>b.Value(), ()=>a.Value()+b.Value()], {type:'translate'});
var tri4 = [];
tri4[0] = board.create('point', [s, move_tri4], {visible: false});
tri4[1] = board.create('point', [tri4[0], left_b], {visible: false});
tri4[2] = board.create('point', [tri4[0], [left_b,down_a]], {visible: false});
var po4 = board.create('polygon',[tri4[0],tri4[1],tri4[2]], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var rot_tri2 = board.create('transform', [function(){return m.Value()*Math.PI/4;}, tri2[0]], {type:'rotate'});
rot_tri2.bindTo([tri2[1],tri2[2]]);

var rot_tri3 = board.create('transform', [function(){return - m.Value()*Math.PI/4;}, tri3_2[0]], {type:'rotate'});
rot_tri3.bindTo([tri3_2[1],tri3_2[2]]);

board.create('segment',[tri2[1], board.create('point', [tri2[1], right_b], {visible: false})],{visible:()=>(m.Value()>=1.99),strokeWidth:1, dash:2});


board.create('text',[()=>s.X()+a.Value()*1/2+b.Value(),()=>s.Y()+b.Value()+1/2*a.Value(),function(){
        return '\\[ a^2 \\]';
    }],{visible: ()=> {return (m.Value()>=1.99);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+a.Value()+1/2*b.Value(),()=>s.Y()+1/2*b.Value(),function(){
    return '\\[b^2\\]';
    }],{visible: ()=> {return (m.Value()>=1.99);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+1/2*(a.Value()+b.Value()),()=>s.Y()+1/2*(a.Value()+b.Value()),function(){
    return '\\[c^2\\]';
    }],{visible: ()=> {return (m.Value()<0.4);}, anchorX: 'middle', anchorY: 'auto'});
""", width=600, height=600, id="jxgbox")

proof_scratchpad_jxg = JSXGraph(code=r"""JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-1, 13, 13, -3], axis:true,grid:true, keepaspectratio:true,  showCopyright:false});

const sx =1, sy = 1;
const a=6, b=4;

var p1, col1, pol1, g1;
col1 = 'red';
p1 = [];
p1.push(board.create('point',[sx, sy+b], {size: 5, strokeColor:'none', fillColor: 'none', withLabel: false}));
p1.push(board.create('point',[sx, sy], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
p1.push(board.create('point',[sx+a, sy], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
pol1 = board.create('polygon', p1, {hasInnerPoints: true, fillColor:col1});
g1 = board.create('group', p1)
g1.setRotationCenter('centroid')
g1.setRotationPoints([p1[0], p1[1], p1[2]]);

board.create('segment',[p1[0],p1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[10, b/2]}});
board.create('segment',[p1[1],p1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a/2, 10]}});
board.create('segment',[p1[2],p1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a/2-10, b/2-10]}});

var p2, col2, pol2, g2;
col2 = 'green';
p2 = [];
p2.push(board.create('point',[sx+a+1, sy], {size: 5, strokeColor:'none', fillColor: 'none', withLabel: false}));
p2.push(board.create('point',[sx+a+1+b, sy], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
p2.push(board.create('point',[sx+a+1+b, sy+a], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
pol2 = board.create('polygon', p2, {hasInnerPoints: true, fillColor:col2});
g2 = board.create('group', p2)
g2.setRotationCenter('centroid')
g2.setRotationPoints([p2[0], p2[1], p2[2]]);

var p3, col3, pol3, g3;
col3 = 'blue';
p3 = [];
p3.push(board.create('point',[sx+a+1+b, sy+a+1], {size: 5, strokeColor:'none', fillColor: 'none', withLabel: false}));
p3.push(board.create('point',[sx+a+1+b, sy+a+1+b], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
p3.push(board.create('point',[sx+1+b, sy+a+1+b], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
pol3 = board.create('polygon', p3, {hasInnerPoints: true, fillColor:col3});
g3 = board.create('group', p3)
g3.setRotationCenter('centroid')
g3.setRotationPoints([p3[0], p3[1], p3[3]]);

var p4, col4, pol4, g4;
col4 = 'yellow';
p4 = [];
p4.push(board.create('point',[sx+b, sy+b+1+a], {size: 5, strokeColor:'none', fillColor: 'none', withLabel: false}));
p4.push(board.create('point',[sx, sy+b+1+a], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
p4.push(board.create('point',[sx, sy+b+1], {size: 5, strokeColor:'none', fillColor:'none', withLabel: false}));
pol4 = board.create('polygon', p4, {hasInnerPoints: true, fillColor:col4});
g4 = board.create('group', p4)
g4.setRotationCenter('centroid')
g4.setRotationPoints([p4[0], p4[1], p4[4]]);
""", width=600, height=600, id="jxgbox")