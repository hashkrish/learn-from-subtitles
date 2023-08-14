export function textToSpeech(text: string) {
	console.log('textToSpeech: ' + text);
	let synth = window.speechSynthesis;

	if (!('speechSynthesis' in window)) {
		alert('Your browser does not support speech synthesis.');
		return;
	}
	if (!synth) {
		synth = window.speechSynthesis;
		console.log('synth: ' + synth);
	}
	let speechObj = new SpeechSynthesisUtterance(text);
	speechObj.voice = synth.getVoices()[10];
	synth.speak(speechObj);
}
