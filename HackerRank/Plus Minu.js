'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    // Write your code here

    arr.sort();
    let dict = {}
    dict["neg"] = 0;
    dict["pos"] = 0;
    dict["zero"] = 0;

    for (let i = 0; i < arr.length; i++) {
        const num = arr[i]
        if (num < 0) {
            dict["neg"] += 1;
        }
        else if (num == 0) {
            dict["zero"] += 1;
        }
        else {
            dict["pos"] += 1;
        }
    }

    const n = arr.length
    let ratios = `${(dict["pos"] / n).toPrecision(6)}\n${(dict["neg"] / n).toPrecision(6)}\n${(dict["zero"] / n).toPrecision(6)}`


    console.log(ratios);


}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
