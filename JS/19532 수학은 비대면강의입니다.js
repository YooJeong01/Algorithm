let [a,b,c,d,e,f] = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);

let x = (e*c-b*f) / (a*e-d*b)
let y = (a*f-d*c) / (a*e-d*b)

console.log(x+' '+y);