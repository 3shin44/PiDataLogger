import request from "./apiCreate";

const api = {
  getVersion: () => {
    return request({
      method: "get", 
      url: "/version"
    });
  },
  startRecord: () => {
    return request({
      method: "get", 
      url: "/startRecord"
    });
  },
  getRecordData: () => {
    return request({
      method: "get", 
      url: "/getRecordData"
    });
  },
  stopRecord: () => {
    return request({
      method: "get", 
      url: "/stopRecord"
    });
  },
};

export default api;
