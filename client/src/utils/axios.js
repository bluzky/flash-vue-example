import axios from 'axios';

/**
 * install axios global instance within Vue app instance
 * @param {App} app: Vue app instance
 * @param {object} options: options to initialize axios instance
 *    - baseUrl: Api base url
 *    - token: optional access token
 */

export default {
  install: (app, options) => {
    app.config.globalProperties.axios = axios.create({
      baseURL: options.baseUrl,
      headers: {
        Authorization: options.token ? `Bearer ${options.token}` : ''
      }
    });
  }
};
