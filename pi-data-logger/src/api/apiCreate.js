import axios from 'axios';

const request = axios.create({   
    baseURL: 'http://192.168.66.14:5000' 
})

export default request