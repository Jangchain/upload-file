// 5
// 3 1 5 7 9
// 8

// const a = 5;
let b = [3, 1, 5, 7, 9];
const c = 8;

let count = 0;

b.sort((a, b) => a - b);
console.log(b);

// for (let i = 0; i < b.length; i++) {
//   const el = b[i];
//   if (el >= c) {
//     count++;
//   }
// }
// if (count > 0) {
//   b.splice(-count);
// }
console.log(b);

// left=0
// [ 1, 2, 3, 5, 7 ]
// right 4
let left = 0;
let right = b.length - 1;
let middle = Math.ceil(b.length);
for (let i = 0; i < b.length; i++) {
  const start = b[left];
  const end = b[right];
  console.log(start, end, count);
  if (left >= right) break;
  if (end >= 8) {
    count++;
    right--;
  } else if (start + end >= 8) {
    left++;
    right--;
    count++;
  } else {
    left++;
  }
}
console.log(count);
