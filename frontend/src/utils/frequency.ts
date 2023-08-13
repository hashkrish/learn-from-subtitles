import { subtitleStore } from '$stores/subtitles';
const ignoreTokens = new Set([
	'!',
	'(',
	')',
	'?',
	'…',
	'→',
	'《',
	'》',
	'！',
	'？',
	'～',
	'～！',
	'｡',
	'の'
]);

let frequency = {};
const subtitleToTokens = (subtitle) => {
	const tokens = subtitle.content.reduce((acc, cur) => {
		if (ignoreTokens.has(cur.token)) {
			return acc;
		}
		acc.push(cur);
		return acc;
	}, []);
	return tokens;
};

export const subtitlesToTokens = (subtitles) => {
	const tokens = subtitles.reduce((acc, cur) => {
		acc.push(...subtitleToTokens(cur));
		return acc;
	}, []);
	return tokens;
};

export const getFrequency = (subtitleStore) => {
	frequency = subtitlesToTokens(subtitleStore).reduce((acc, cur) => {
		acc[cur?.token] = acc[cur?.token] || cur;
		acc[cur?.token].frequency = (acc[cur?.token].frequency || 0) + 1;
		// console.log(acc[cur?.token]);
		return acc;
	}, {});
	// console.log(frequency);
	return frequency;
};

export const getOrderedTokensByFrequency = (frequency) => {
	let orderedWordsByFrequency = Object.keys(frequency)
		.sort((a, b) => frequency[b].frequency - frequency[a].frequency)
		.map((key) => frequency[key]);
	// console.log('gow:', orderedWordsByFrequency);
	return orderedWordsByFrequency;
};
