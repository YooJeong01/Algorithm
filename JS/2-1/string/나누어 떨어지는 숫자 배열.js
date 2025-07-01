



solution([5,9,7,10], 5)
solution([2, 36, 1, 3], 1)
solution([3,2,6], 10)

function solution(arr,divisor){
    let result = []
    arr.forEach((number) => {
        if(number%divisor === 0) result.push(number)
    });
    result.sort((a,b)=>a-b)

    result.length>0 ? console.log(result) : console.log([-1])
}

