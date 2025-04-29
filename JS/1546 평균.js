function solution1(){
    const fs = require('fs');
    const [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    const inputArr = input.trim().split(" ").map(Number);
    
    let sum = 0;
    maxScore = Math.max(...inputArr);
    for (let i of inputArr) {
        i = i/maxScore*100
        sum += i;
    }
    
    console.log(sum/inputArr.length); 
}

function solution2(){
    const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');
    const score = input[1].split(' ').map(Number);
    const maxScore = Math.max(...score);
    const newScore = score.map(x => x/maxScore*100);
    
    const sum = newScore.reduce((prev, curr)=> prev + curr);
    const avg = sum/newScore.length;
    console.log(avg);
}


