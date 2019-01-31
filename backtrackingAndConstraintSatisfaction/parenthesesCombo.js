const results = [];
const currentAnswer = [];
const stack = [];

function dfs(n) {
    if (currentAnswer.length === n * 2 && stack.length === 0) {
        return results.push(currentAnswer.join(""));
    }

    if (currentAnswer.length === n * 2 && stack.length !== 0) {
        return;
    }

    currentAnswer.push("(");
    stack.push("(");

    dfs(n);

    currentAnswer.pop("(");
    stack.pop("(");


    if (stack[stack.length - 1] === "(") {
        currentAnswer.push(")");
        stack.pop();

        dfs(n);

        currentAnswer.pop(")");
        stack.push("(");
    }
}

dfs(10)
console.log(results.length, 'RESULTS');