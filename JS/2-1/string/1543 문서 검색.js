// https://www.acmicpc.net/problem/1543

solution('ababababa','aba')
solution('a a a a a','a a')
solution('ababababa','ababa')
solution('aaaaaaa','aa')

// 백준 입력 받는 코드
// const readFile = process.platform === 'linux' ? '/dev/stdin' : 't.txt';

// let [input, target] = require('fs')
//   .readFileSync(readFile)
//   .toString()
//   .trim()
//   .split('\\n');

function solution(input, word){

    let idx = 0;
    let count = 0;
    while(idx<input.length){
        // idx부터 끝까지 잘라내서
        // word가 처음으로 등장하는 위치 index를 반환 없으면 -1 반환
        const target = input.slice(idx).search(word)
        //console.log(`target : ${target}`);
        if(target>= 0) { // word 존재시
            count++;
            idx += target + word.length; // 다음에 시작할 위치 포인터를 옮겨주기
        } else break;
    }
    console.log(count);
}

// 백준 출력하는 코드
// solution(input, target);