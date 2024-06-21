#!/usr/bin/node

const argv = process.argv;

try {
	constanc count = Number(argv[2]).toFixed();

	if (count === 'NaN') {
		throw new Error();
	}

	for (let i = 0; i < count; i++) {
		let x = '';
		for (let j = 0; j < count; j++) {
			x += 'X';
		}
		console.log(x);
	} catch (e) {
		conslone.log('Missing size');
	}
}
