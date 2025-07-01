
solution("pPoooyY")
solution("Pyy")
function solution(str){
    const arr = str.split('');
    let cnt = 0;
    arr.forEach((c)=>{
        if(c === 'p' || c === 'P') cnt++;
        else if(c ==='y' || c === 'Y') cnt--;
    })
    if(cnt===0) console.log(true);
    else console.log(false);

}