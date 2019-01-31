
const possibleIps = [];

function findIpList(ipstr) {
    let iplist = ipstr.split("").reduce((arr, char) => {
        arr.push(char, "");
        return arr;
    }, []);
    iplist.pop();

    dfs(iplist, 0, 0);

    return possibleIps;
}

function constructNumber(arr, i) {
    let accum = 0;
    for (let j = i; j < arr.length; j += 2) {
        accum = accum * 10;
        accum = accum + +arr[j];
    }
    return accum;
}

function dfs(arr, i, level) {
    if (level === 3 && constructNumber(arr, i) <= 255 && i < arr.length) {
        return possibleIps.push(arr.join(""));
    }
    let j = i;
    let accum = arr[j];
    while (accum <= 255 && j < arr.length) {
        arr[j + 1] = ".";
        dfs(arr, j + 2, level + 1);
        arr[j + 1] = "";
        accum = accum * 10;
        accum = accum + +arr[j];
        j += 2;
    }
}

console.log(findIpList("5215022"));
// console.log(findIpList("11111"));

