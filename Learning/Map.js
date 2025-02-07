Array.prototype.myMap = function (callback) {
    const toReturn = [];
    for (let i = 0; i < this.length; i++) {
        toReturn.push(callback(this[i]));
    }
    return toReturn;
}


const logAndReturn = x => {
    console.log(x);
    return x;
};
const arr1 = [1, 2, 3, 4, 5].myMap(logAndReturn);
const arr2 = ['a', 'b', 'c'].myMap(logAndReturn);

console.log(arr1);
console.log(arr2);