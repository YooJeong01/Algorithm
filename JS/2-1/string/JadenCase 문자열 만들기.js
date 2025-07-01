function solution(s){
    // 문자 입력받기
    // 알파벳이면 대문자로 바꾸기
    // 띄어쓰기로 문자 자르기
    const words = s.split(' ');
    const newWords = [];

    words.forEach((word)=>{
        const char1 = word[0].toUpperCase();
        const char2 = word.slice(-word.length+1).toLowerCase();
        const joinWord = char1.concat(char2)
        // console.log(joinWord);
        newWords.push(joinWord);
    })
    console.log(newWords.join(' '));
    
}

solution("3people unFollowed me")
solution("for the last week")