function FizzBuzz() {
    // Your code here
    // For numbers 1 to n:
    // If number is divisible by 3, print "Fizz"
    // If number is divisible by 5, print "Buzz"
    // If number is divisible by both 3 and 5, print "FizzBuzz"
    // Otherwise, print the number itself
    for (let n = 0; n < 100; n++) {
        let result = ""
        if (n === 0) {
            result = result.concat(n);
        }

        else if (n % 3 === 0) {
            result = result.concat("Fizz");
        }
        else if (n % 5 === 0) {
            result = result.concat("Buzz");
        }
        else {
            result = result.concat(n);
        }
        console.log(result);
    }
}


function simpleFizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        let out = "";

        if (i % 3 === 0) {
            out += "Fizz";
        }
        if (i % 5 === 0) {
            out += "Buzz";
        }
        if (out === "") {
            out = i;
        }
        console.log(out || i);
    }
}

FizzBuzz();