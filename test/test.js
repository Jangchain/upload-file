// 5
// b a
// c a
// d c
// e c
// f d
// c

const lists = [
  ["b", "a"],
  ["c", "a"],
  ["d", "c"],
  ["e", "c"],
  ["f", "d"],
];

const obj = {
  a: {
    b: {},
    c: {
      d: {},
      e: {
        f: {},
      },
    },
  },
};

const key = "c";
const tempObj = {};
for (let i = 0; i < lists.length; i++) {
  const el = lists[i];
  if (!tempObj[el[1]]) {
    tempObj[el[1]] = {};
    tempObj[el[1]][el[0]] = {};
  } else {
    tempObj[el[1]][el[0]] = {};
  }
}
console.log(tempObj);
console.log(tempObj[key]);
const result = [];
let tempRes = [...Object.keys(tempObj[key])];
while (tempRes.length) {
  result.push(...tempRes);
  const temp1 = [];
  for (let i = 0; i < tempRes.length; i++) {
    const element = tempRes[i];
    tempObj[element] && temp1.push(...Object.keys(tempObj[element]));
  }
  tempRes = temp1;
}

console.log(result);
