export function get_jwt() {
    let jwt = "";
    axios
        .post("http://localhost:8001/api/v1/jwt", {
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
    localStorage.setItem("jwt", jwt);
}

export function get_jwt_from_localstorage() {
    return localStorage.getItem("jwt");
}
