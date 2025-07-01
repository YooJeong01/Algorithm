function solution(s){
    let ary = s.split('');
    let length = ary.length;
    if(length % 2 !== 0) return false;
    if(ary[length-1] === '(') return false;
    if(ary[0] === ')') return false;

    let flag = 0;
    while(length>=0){
        let target = ary.pop()
        if(target === ')') flag++;
        if(target === '(') flag--;
        length--;
    }
    if(flag===0) return true;
    else return false;
}

const answer = solution("(())()")
console.log(answer)





// gpt 도움 받은 코드
// for of를 쓰자..
function solution2(s){
    let left = [];
    for(let char of s){
        if(char==='('){
            left.push(char);
        }else{
            if(left.length === 0) return false;
            left.pop();
        }
    }

    if(left.length === 0) return true;
    else return false;
}

const answer2 = solution2("(())()")
console.log(answer2)