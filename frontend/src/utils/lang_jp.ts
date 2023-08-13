// set type
const half_to_full_width: { [key: string]: string } = {
	'｡': '。',
	'｢': '「',
	'｣': '」',
	'､': '、',
	'･': '・',
	ﾞ: '゛',
	ﾟ: '゜',
	ｰ: 'ー',
	ｧ: 'ァ',
	ｱ: 'ア',
	ｨ: 'ィ',
	ｲ: 'イ',
	ｩ: 'ゥ',
	ｳ: 'ウ',
	ｳﾞ: 'ヴ',
	ｪ: 'ェ',
	ｴ: 'エ',
	ｫ: 'ォ',
	ｵ: 'オ',
	ｶ: 'カ',
	ｶﾞ: 'ガ',
	ｷ: 'キ',
	ｷﾞ: 'ギ',
	ｸ: 'ク',
	ｸﾞ: 'グ',
	ｹ: 'ケ',
	ｹﾞ: 'ゲ',
	ｺ: 'コ',
	ｺﾞ: 'ゴ',
	ｻ: 'サ',
	ｻﾞ: 'ザ',
	ｼ: 'シ',
	ｼﾞ: 'ジ',
	ｽ: 'ス',
	ｽﾞ: 'ズ',
	ｾ: 'セ',
	ｾﾞ: 'ゼ',
	ｿ: 'ソ',
	ｿﾞ: 'ゾ',
	ﾀ: 'タ',
	ﾀﾞ: 'ダ',
	ﾁ: 'チ',
	ﾁﾞ: 'ヂ',
	ｯ: 'ッ',
	ﾂ: 'ツ',
	ﾂﾞ: 'ヅ',
	ﾃ: 'テ',
	ﾃﾞ: 'デ',
	ﾄ: 'ト',
	ﾄﾞ: 'ド',
	ﾅ: 'ナ',
	ﾆ: 'ニ',
	ﾇ: 'ヌ',
	ﾈ: 'ネ',
	ﾉ: 'ノ',
	ﾊ: 'ハ',
	ﾊﾞ: 'バ',
	ﾊﾟ: 'パ',
	ﾋ: 'ヒ',
	ﾋﾞ: 'ビ',
	ﾋﾟ: 'ピ',
	ﾌ: 'フ',
	ﾌﾞ: 'ブ',
	ﾌﾟ: 'プ',
	ﾍ: 'ヘ',
	ﾍﾞ: 'ベ',
	ﾍﾟ: 'ペ',
	ﾎ: 'ホ',
	ﾎﾞ: 'ボ',
	ﾎﾟ: 'ポ',
	ﾏ: 'マ',
	ﾐ: 'ミ',
	ﾑ: 'ム',
	ﾒ: 'メ',
	ﾓ: 'モ',
	ｬ: 'ャ',
	ﾔ: 'ヤ',
	ｭ: 'ュ',
	ﾕ: 'ユ',
	ｮ: 'ョ',
	ﾖ: 'ヨ',
	ﾗ: 'ラ',
	ﾘ: 'リ',
	ﾙ: 'ル',
	ﾚ: 'レ',
	ﾛ: 'ロ',
	ﾜ: 'ワ',
	ｦ: 'ヲ',
	ｦﾞ: 'ヺ',
	ﾝ: 'ン'
};

const half_to_full_width_set = new Set(Object.keys(half_to_full_width));

export function convertToFullWidth(text: string) {
	let full_width_text = '';
	for (let i = 0; i < text.length; i++) {
		let char = text[i];
		if (half_to_full_width_set.has(char)) {
			try {
				if (char in ['ﾞ', 'ﾟ']) {
					char = text[i - 1] + char;
					full_width_text = full_width_text.slice(0, -1);
				}
				full_width_text += half_to_full_width[char];
			} catch (e) {
				console.log(e);
				full_width_text += char;
			}
		} else {
			full_width_text += char;
		}
	}
	return full_width_text;
}
