// 여기서 .trim() 안해주면 공백 줄이 들어갈수도 있다
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(a => Number(a));
const T = input[0]
const where = []
for(let i=1; i<input.length; i+=2){
    where.push([input[i],input[i+1]]);
}
for(let w of where){
    let k = w[0];
    let n = w[1];
    
    let people = [];
    for(let i=0; i<n; i++){
        people[i]=i+1;
    }

    for(let x=0; x<k; x++){
        for(let y=0; y<n; y++){
            if( y===0 ) continue;
            people[y] += people[y-1];
        }
    }
    console.log(people[people.length-1]); // js는 [-1]인덱싱을 지원하지 않는다
}

// 다른 사람 풀이
// 2차원 방식으로 품
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
// const T = input.shift();
// for (let i = 0; i<T; i++) {
//     const k = input.shift();
//     const n = input.shift();

//     //2차원 배열 생성 및 초기화
//     const apt = Array.from(Array(k+1), ()=>Array(n+1).fill(0));
//     apt[0].forEach((_, index) => apt[0][index] = index);

//     for(let x=1; x<=k; x++){
//         for(let y=1; y<=n; y++){
//             apt[x][y] = apt[x-1][y] + apt[x][y-1];
//         }
//     }

//     console.log(apt[k][n]);
// }