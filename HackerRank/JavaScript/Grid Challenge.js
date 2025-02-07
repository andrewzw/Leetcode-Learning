'use strict';

/**
 * @param {number[]} grid - Array of profit values
 * @returns {number} - Number of pairs that sum to target
 */
function gridChallenge(grid) {
    // Write your solution here

    let sorted_grid = []
    for (let row = 0; row < grid.length; row++) {
        sorted_grid.push(grid[row].split('').sort())
    }

    for (let col = 0; col < sorted_grid[0].length; col++) {
        for (let row = 1; row < sorted_grid.length; row++) {
            if (sorted_grid[row - 1][col] > sorted_grid[row][col]) {
                return "NO"
            }
        }
        return "YES"
    }
}
const grid1 = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
const grid2 = ["abc", "lmp", "qrt"]
console.log(gridChallenge(grid1));
console.log(gridChallenge(grid2));
