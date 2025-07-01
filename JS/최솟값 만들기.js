function solution(s) {
    // split 기준을 띄어쓰기로 해서 리스트로 받기
    // 첫문자 검사하기
    // 영어면 첫문자 대문자로 바꾸기
    // join으로 출력?

    // str.charAt(index)은 index 위치의 문자의 값을 가져옴
    // 없으면 빈 문자열을 반환함 => undefind가 아니기 때문에 에러처리에 유연하다
    let ary = s.split(' ');
    let answer = ary.map((a)=>a.charAt(0).toUpperCase() + a.slice(1).toLowerCase())
    return answer.join(' ');
    

    // 아래 코드가 틀린 이유는 charAt(0)으로 특정 인덱스를 바로 가져와주는데 str[0]으로 했기 때문..
    // ary.forEach((str)=>{
    //     if( ! (/[0-9]/.test(str[0]))) {
    //         let newStr = str[0].charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    //         answer.push(newStr)
    //     } else {
    //         answer.push(str)
    //     }
    // })
}


solution('"for    the    last week"') 
// For   The   Last Week
solution("3people unFollowed me");
// 3people Unfollwed Me