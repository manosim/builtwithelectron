var request = require('superagent');

var apiRequests = {
  get: function (url) {
    return request
      .get(url)
      .set('Accept', 'application/json');
  },

  post: function (url, params, csrfToken, coverPath) {
    return request
      .post(url)
      .send(params)
      .attach('cover', coverPath)
      .set('X-CSRFToken', csrfToken)
      .set('Accept', 'application/json');
  }
};

module.exports = apiRequests;
