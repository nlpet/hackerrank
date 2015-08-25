function closestNumber(arr) {
   var a = parseInt(arr[0]),
       b = parseInt(arr[1]),
       x = parseInt(arr[2]),
       c = Math.pow(a, b),
       d = c % x,
       under = parseInt(c - d),
       over = under + x;
    
    if (c - under <= over - c) {
        console.log(under);
    } else {
        console.log(over);
    }
}

function processData(input) {
    inputArray = input.split('\n');
    T = parseInt(inputArray[0]);
    for (var i = 1; i <= T; i++) { 
        closestNumber(inputArray[i].trim().split(' '));
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
