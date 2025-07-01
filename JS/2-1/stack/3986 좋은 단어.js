// 무조건 겹치는 경우 abababab 좌나 우에 같은게 존재하지 않고 무조건 다른경우
// 단어 길이가 홀수면 안됨
// 괄호 스택 문제랑 같은 느낌인듯?

solution("ABAB AABB ABBA")
solution("AAA AA AB")
solution("ABBABB")

function solution(str){
    const word_list = str.split(' ');
    let count = 0;

    word_list.forEach((word)=>{
        if(word.length%2===0){
            const stack = []
            for(let c of word){
                if(stack.length<=0) stack.push(c)
                else{
                    const popChar = stack.pop();
                    if(popChar!==c) {
                        stack.push(popChar);
                        stack.push(c);
                    }
                }
            }
            console.log(stack);
            
            if(stack.length === 0){
                count++;
            }
        }
    })
    console.log(count);
}


// 설명 주석용
function solution3(str){
    // 1. 공백을 기준으로 단어들을 담은 배열 생성
    const word_list = str.split(' ');
    // 2. 좋은 단어를 카운트할 변수 생성
    let count = 0;

    // 3. 단어들을 담은 배열 순회
    word_list.forEach((word)=>{
        // 4. 단어 하나에 대해서 아래 작업 수행
        // 5. 단어 길이에 따라 짝수(좋은단어), 홀수(나쁜단어) 분류
        if(word.length%2===0){

            // 6. 단어마다 스택 비워줘야하니, 여기서 초기화
            const stack = []

            // 7. 단어 하나의 한 글자씩 검사
            for(let c of word){

                // 8. 스택에 아무것도 없는 경우에는 push
                if(stack.length<=0) stack.push(c)

                // 9. 스택에 하나라도 존재한다면 맨 마지막 꺼 꺼내기
                else{
                    // 10. 맨 마지막(스택 최상단) 단어 꺼내기
                    const popChar = stack.pop();
                    
                    // 11. 현재 문자(c)와 꺼낸 문자(popChar)가 같은지 비교
                    // 12. 같지 않다면
                    if(popChar!==c) {
                        // 13. 모두 스택에 다시 넣어주기
                        stack.push(popChar);
                        stack.push(c);
                    }
                    // 13. 같다면 스택에 둘 다 넣지 않고 종료
                }
            }
            // 디버깅용 콘솔 로그 
            console.log(stack);
            
            // 14. 스택이 남아있는 문자(c)가 없는 경우 좋은 단어로 판정
            if(stack.length === 0){
                count++;
            }
        }
    })
    console.log(count);
}

solution3("ABAB AABB ABBA")
solution3("AAA AA AB")
solution3("ABBABB")


// 백준 제출용 코드
// 백준 출력은 console.log다!!>...
// let [N, ...word_list] = require("fs").readFileSync("/dev/stdin").toString().trim().split('\n');
// N = Number(N)

// function solution2(N, word_list){
//     let count = 0;
//     word_list.forEach((word)=>{
//         if(word.length%2===0){
//             const stack = []
//             for(let c of word){
//                 if(stack.length<=0) stack.push(c)
//                 else{
//                     const popChar = stack.pop();
//                     if(popChar!==c) {
//                         stack.push(popChar);
//                         stack.push(c);
//                     }
//                 }
//             }
            
//             if(stack.length === 0){
//                 count++;
//             }
//         }
//     })
//     return count;
// }

// const answer = solution2(N,word_list);
// console.log(answer);