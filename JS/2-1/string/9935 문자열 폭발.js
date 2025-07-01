/**
 * 백준 9935 문자열 폭발
 * https://www.acmicpc.net/problem/9935
 * 
 * hint
 * 1. for of로 문자 하나씩 스택에 넣기
 * 2. 스택의 제일 마지막에서 비교하고자 하는 key 길이만큼만 꺼내기
 * 3. 꺼낸 단어와 key가 같은지 비교
 * 4. 같다면 splice로 제거하기
 */
// 백준 입력
// const readFile = process.platform === 'linux' ? '/dev/stdin' : 't.txt';

// let [str, key] = require('fs')
//   .readFileSync(readFile)
//   .toString()
//   .trim()
//   .split('\\n');
  
function explosion(str, key){
      const stack = []; 
      const k = key.length; // 폭발 문자열 길이
      
      for (const c of str) {
          stack.push(c);
          
          // 스택 끝 k개의 글자만 꺼내서 key(폭발 문자열)와 비교
          // 스택의 길이가 k개 이상이고,
          // 스택 제일 뒤에서 k개 만큼 잘라서 뽑아온 후
          // join을 했을때 문자열이
          // 폭발 문자열과 같다면
          if (stack.length >= k && stack.slice(-k).join('') === key) {
              // 일치하면 그 자리에서 바로 제거
              stack.splice(stack.length - k, k);
            }
    }
    if (stack.length == 0) console.log("FRULA")
    else console.log(stack.join(''));
}



explosion('mirkovC4nizCC44','C4')
explosion('12ab112ab2ab', '12ab')

// 백준 출력
// explosion(str,key)


/**
 * 
 * 스택에 문자열을 하나씩 쪼개서 담는다
 * 맨 처음부터 꺼낸다
 * 꺼낸 갯수가 key와 같아질때 key와 단어가 같은지 비교한다
 * 꺼낸 갯수가 key보다 많아질때는 key 길이만큼만 이동하면서 비교한다
 * 같은게 있다면 해당 문자를 없앤다 splice or pop 등
 * 포인터는 key의 길이보다 한칸 적게 위치하고있다
 * 폭발시킨후 거기서 부터 다시 비교한다
 */

// const arr = []
// let word_start = 0;
// let word_finish = key.length;
// let start = arr.length-key.length;
// let finish = key.length-1;


// for(let c of str){
//     arr.push(c);
//     if(arr.length < key.length) continue; 

//     word = [...arr].slice(word_start,word_finish).join('')        

//     if(word === key){
//         console.log(word);
//         arr.splice(start, key.length);
//     }
//     word_start ++;
//     word_finish ++;
//     console.log(arr);
// }