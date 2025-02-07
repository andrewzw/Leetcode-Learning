'use strict';

/**
 * @param {number[]} stocksProfit - Array of profit values
 * @param {number} target - Target profit value
 * @returns {number} - Number of pairs that sum to target
 */
function stockPairs(stocksProfit, target) {
    // Write your solution here
    stocksProfit.sort((a, b) => a - b);
    const n = stocksProfit.length;
    let right = 0;
    let left = n - 1;
    const pairs = new Set();

    while (right < left) {
        const sum = stocksProfit[right] + stocksProfit[left];
        if (sum === target) {
            pairs.add(`${stocksProfit[right]},${stocksProfit[left]}`)
            left += 1;
            right += 1;
        } else if (sum > target) {
            left -= 1;
        } else {
            right += 1;
        }

    }
    console.log(pairs.size);
    console.log(pairs);
}

const stockProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
const target = 12
stockPairs(stockProfit, target);
// Example usage:
// const profits = [5, 7, 9, 13, 11, 6, 6, 3, 3];
// const targetProfit = 12;
// console.log(stockPairs(profits, targetProfit));