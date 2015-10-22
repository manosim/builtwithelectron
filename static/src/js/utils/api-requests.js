var request = require('superagent');

var apiRequests = {
  get: function (url) {
    return request
      .get(url)
      .set('Accept', 'application/json');
  },

  post: function (url, params, csrfToken) {
    return request
      .post(url)
      .send(params)
      .set('X-CSRFToken', csrfToken)
      .set('Accept', 'application/json');
  }
};

module.exports = apiRequests;
