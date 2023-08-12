import { APIURL } from '../config';
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
