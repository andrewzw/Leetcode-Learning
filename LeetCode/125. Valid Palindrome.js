/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    console.log(cleaned);
    return (cleaned === cleaned.split("").reverse().join(""))
};