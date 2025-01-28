function generateRandomString({ size, num }) {
    let result = '';
    for (let i = 0; i < size; i++) {
        result += num[Math.random() * num.length | 0];
    }
    return result;
}

function getFinger(input, selectionCount) {
    let selected = [];
    let remainingLength = input.length;

    for (let i = 0; i < input.length && selectionCount > 0; i++) {
        if (Math.random() * remainingLength < selectionCount) {
            selected.push(input[i]);
            selectionCount--;
        }
        remainingLength--;
    }

    let shuffled = '';
    for (let i = 0; i < selected.length; i++) {
        const randomIndex = Math.random() * (selected.length - i) | 0;
        shuffled += selected[randomIndex];
        selected[randomIndex] = selected[selected.length - i - 1];
    }

    let unused = '';
    for (let char of input) {
        if (!shuffled.includes(char)) {
            unused += char;
        }
    }

    const randomLength = Math.random() * input.length | 0;
    const fpFirst = generateRandomString({ size: randomLength, num: unused });
    const fpThird = generateRandomString({ size: 11 - randomLength - 1, num: unused });

    const fingerprint = (fpFirst + shuffled + fpThird + randomLength).split("");
    const part1 = fingerprint.slice(0, 14);
    const part2 = fingerprint.slice(14);

    let result = '';
    while (part1.length > 0) {
        result += (35 - parseInt(part1.pop(), 36)).toString(36);
    }

    result += part2.join('');
    return result;
}

const inputString = 'qw3pa2mn87';
const selectionCount = 5;
console.log(getFinger(inputString, selectionCount));
