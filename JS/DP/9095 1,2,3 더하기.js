
// 숫자형으로 바꾸려고 *1 했다가 배열*1 = NaN으로 연산이 되어서
// input[@] = undefined가 됐다.. ㅎ
// 배열일땐 정석으로 형변환 해주기!
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number)
const T = input[0]
for(let t=1; t<T+1; t++){
    const n = input[t];
    let arr = new Array(n+1).fill(0);
    for(let i=1; i<n+1; i++){
        if (i===1) arr[i] = 1
        else if (i===2) arr[i] = 2
        else if (i===3) arr[i] = 4
        else
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    }
    console.log(arr[n])
}

// js는 리스트가 동적으로 늘어나기 때문에 없는 인덱스에 값 넣기가 가능하다
// 하지만 파이썬은 고정되어 있어서 IndexError가 난다. 그래서 미리 크기를 만들어둬야한다
// ⬇ 이런게 가능함
// const occation = [0];
// occation[1] = 1;
// occation[2] = 2;
// occation[3] = 4;