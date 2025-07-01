

function solution(s){
    // 문자 공백 기준 잘라서 배열에 넣기
    // 배열 맨 마지막 요소 잡기
    // 길이 반환하기

    const arr = s.trim().split(' ');
    console.log(arr[arr.length-1].length);
}


solution("Hello World");
solution("   fly me   to   the moon  ");
solution("luffy is still joyboy");