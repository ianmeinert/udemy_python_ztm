// Api.js
import axios from "axios"

// Create an instance of axios to use the same base url.
let baseURL = "http://localhost:8000" // it's not recommended to have this info here.


// function to execute the http get request
const get = (url, request) => axios.get(url = baseURL + url, request = request);

// function to execute the http delete request
const deleteRequest = (url, request) => axios.delete(url = baseURL + url, request = request);

// function to execute the http post request
const post = (url, request) => axios.post(url = baseURL + url, request = request);

// function to execute the http put request
const put = (url, request) => axios.put(url = baseURL + url, request = request);

// function to execute the http path request
const patch = (url, request) => axios.patch(url = baseURL + url, request = request);

// expose your method to other services or actions
const API = {
    get,
    delete: deleteRequest,
    post,
    put,
    patch
};
export default API;