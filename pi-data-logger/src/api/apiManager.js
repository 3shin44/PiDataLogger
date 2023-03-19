import request from "./apiCreate";

const api = {
  getVersion: () => {
    return request({
      method: "get", 
      url: "/version"
    });
  },
};

export default api;
