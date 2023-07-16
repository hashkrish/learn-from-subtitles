const NODE_ENV = process.env.NODE_ENV || "production";

export const BASEURL =
    NODE_ENV === "production"
        ? "https://lrs.centralindia.cloudapp.azure.com"
        : "http://localhost:8001";
export const APIURL = BASEURL + "/api/v1";
