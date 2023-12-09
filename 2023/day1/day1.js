const fs = require('fs').promises

const part1 = async () => {
    const inputPath = __dirname + '/part1.txt';
    const inputText = await fs.readFile(inputPath, 'utf-8');

    const sum = inputText.split('\n').reduce((acc, curr, i) => {
        curr = curr.replace(/[^\d]/g, '')
        let toAdd;

        const firstDigit = curr.match(/\d/);
        const lastDigit = curr.match(/\d(?=[^\d]*$)/);

        toAdd = Number.parseInt(firstDigit.toString() + lastDigit.toString());

        acc += toAdd;
        return acc;
    }, 0);
    console.log("Part1:", sum);
}


const stringToStringNumber = (str) => {
    if (IS_NUMBER.test(str)) return str;

    const numbers = {
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9
    }
    return (numbers[str]).toString();
}

const sample = `twone`

const part2 = async () => {
    const inputPath = __dirname + '/part1.txt';
    const inputText = await fs.readFile(inputPath, 'utf-8');
    IS_NUMBER = /^\d+$/;

    const sum = inputText.split('\n').reduce((acc, curr, i) => {
        curr = curr.matchAll(/(?=(\d|one|two|three|four|five|six|seven|eight|nine))/g);
        curr = Array.from(curr, match => match[1])
        const firstValue = curr[0];
        const lastValue = curr[curr.length - 1];

        const first = stringToStringNumber(firstValue);
        const last = stringToStringNumber(lastValue);

        const combined = first + last;
        const asNumber = Number.parseInt(combined);

        // console.log({ raw: curr, first, last, combined, asNumber, i });

        acc += asNumber
        return acc;

    }, 0);

    console.log("Part2:", sum);
}

part1();
part2();