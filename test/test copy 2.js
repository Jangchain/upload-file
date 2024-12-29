// n k
// n 1-9   k 1-n!
const n = 3;
const k = 3;
const list = [];
for (let i = 1; i <= n; i++) {
  list.push(i);
}
console.log(list);
if (list.length === 1) {
  console.log(n);
  //   return;
}

let all = [];

function allList(list, num) {
  if (!list.length) {
    all.push(num);
    return;
  }
  for (let i = 0; i < list.length; i++) {
    let arr1 = list.slice(0, i);
    let arr2 = list.slice(i + 1);
    let tempArr = [...arr1, ...arr2];
    // console.log("tempArr", tempArr);
    allList(tempArr, num + list[i]);
  }
}
allList(list, "");
// console.log(all);
console.log(all.sort()[k - 1]);
const dd = new Array(n).fill(0).map((_, i) => i + 1);
console.log(dd);
