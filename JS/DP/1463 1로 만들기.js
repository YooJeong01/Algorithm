const n = require('fs').readFileSync('/dev/stdin').toString().trim()*1

// 아래 리스트는 실행시간이랑 메모리가 너무 커짐
// let dp = Array.from({length : 10000001}, ()=>0)
let dp = new Array(n+1).fill(0) // 최소한의 크기의 리스트만 생성하기

for(let i=2; i<n+1; i++){
    dp[i] = dp[i-1]+1
    if(i%3 == 0) {
        dp[i] = Math.min(dp[i],dp[i/3]+1)
    }
    if(i%2 == 0) {
        dp[i] = Math.min(dp[i],dp[i/2]+1)
    }
}

console.log(dp[n])