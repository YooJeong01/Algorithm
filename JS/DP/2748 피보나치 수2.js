// 실패한 풀이
// const n = Number(require('fs').readFileSync('/dev/stdin').toString().trim());
// // 1차원 배열 생성및 초기화
// let ans = Array.from({ length: n+1 }, ()=>0)
// ans[1] = 1
// if(n>=2){
//     for(let i=2; i<n+1; i++){
//         ans[i] = ans[i-1] + ans[i-2]
//     }
// }
// console.log(ans[n+1])


// 다른 풀이
// js는 90의 피보나치수를 담을 수 없다. 표현할 수 있는 수의 범위를 넘어선다
// 그래서 BigInt로 객체 형식으로 바꾸어 계산해야한다

const n = require('fs').readFileSync('/dev/stdin').toString()*1;
//const n = 17
const dp = [0,1];
for(let i=2; i<n+1; i++){
    dp[i] = BigInt(dp[i-1])+ BigInt(dp[i-2]);
}
console.log(dp[n].toString());
console.log(typeof(dp[n].toString()));