function solution(s) {
    const str = s.split(' ');
    let num = []
    str.forEach((s)=>{
        num.push(parseInt(s))
    })  

    let minNum = num[0];
    let maxNum = num[0];
    for(let i =0; i<num.length; i++){
        minNum = Math.min(num[i],minNum)
        maxNum = Math.max(num[i],maxNum)
    }
    var answer = minNum + ' ' + maxNum;
    return answer;
}

const answer = solution("1 2 3 4")
console.log(answer)