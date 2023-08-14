import { localCache } from '$src/stores/cache';
import { APIURL } from '../config';
import axios from 'axios';

export function get_jwt() {
	let jwt = '';
	axios
		.post(`${APIURL}/jwt`, {
			text: text
		})
		.then((response) => {
			jwt = response.data.token;
		})
		.catch((error) => {
			console.log(error);
		});
	store_jwt_to_localstorage(jwt);
	return jwt;
}

export function store_jwt_to_localstorage(jwt) {
	localStorage.setItem('jwt', jwt);
}

export function get_jwt_from_localstorage() {
	return localStorage.getItem('jwt');
}

export function remove_jwt_from_localstorage() {
	localStorage.removeItem('jwt');
}

export function get_jwt_from_sessionstorage() {
	return sessionStorage.getItem('jwt');
}

export function store_jwt_to_sessionstorage(jwt) {
	sessionStorage.setItem('jwt', jwt);
}

export function remove_jwt_from_sessionstorage() {
	sessionStorage.removeItem('jwt');
}
export async function getWordTranslation(word, from, to) {
	from = from || 'ja';
	to = to || 'en';

	// if (debouncedAPICall) {
	// 	debouncedAPICall.cancel();
	// }
	//
	// debouncedAPICall = debounce(async (word: string, from: string, to: string) => {

	const url = `${APIURL}/translate/${from}/${to}?word=${word}`;
	const response = await axios.get(url);

	if (response.status === 200) {
		let lc = localCache.subscribe((value) => {
			value[word] = response.data[0]?.meaning.replaceAll(':', ', ') || 'Not found';
		});
		return response.data;
	} else {
		return null;
	}

	lc();

	// }, 500);
	// debouncedAPICall(word, from, to);
}
