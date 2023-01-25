/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let reversed = x.toString().replace('-', '').split('').reverse().join('');
    if (x.toString()[0] === '-'){
        reversed = '-' + reversed;
    }
    if (~~reversed === Number(reversed)){
        return ~~reversed;
    }
    return 0;
};


// 다른 사람의 풀이 1
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let getArray = x.toString().split("")

   
        let getReverseArray=[]
    for(let i= getArray.length-1;i>=getArray.includes("-")?1:0;i--){
       getReverseArray.push(getArray[i]) 
    }
 getArray.includes("-")?getReverseArray.unshift("-"):getReverseArray
      let getint= getReverseArray.join("")

   

    
    if(getint > Math.pow(2,31) || getint < Math.pow(-2,31)) {
        return 0;
    }  else{
           return getint
    }

};



// 다른 사람의 풀이 2
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    isNegative = x<0;
    ans = 0 
    n = 1
    x = Math.abs(x)

    

    while(x > 0) {
        num = x % 10;
        ans *= 10
        ans += num;
        x = Math.floor(x / 10);
        
       
    }
    if(ans > 2147483648) {
        return 0
    }
    if(isNegative) {
        return ans*-1
    }
    return ans

};
