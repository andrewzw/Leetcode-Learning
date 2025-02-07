/*
    1. [[1], [2]] = [1, 2]
    2. [[1, [2]], [5]] = [1, 2, 5]

*/

Array.prototype.flatten = function () {
    const result = [];
    for (let i = 0; i < this.length; i++) {
        if (Array.isArray(this[i])) {
            const value = this[i].flatten();
            result.push(...value);

        }
        else if (typeof this[i] === 'number') {
            result.push(this[i]);

        }

    }

    return result;
}

console.log([].flatten());
console.log([[1], [2]].flatten());
console.log([1, 2, 3].flatten());
console.log([[1, 2], 3, 4].flatten());
console.log([[1, 2], [3, [4, 5]], 6].flatten());

