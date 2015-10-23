var request = require('superagent');

var apiRequests = {
  get: function (url) {
    return request
      .get(url)
      .set('Accept', 'application/json');
  },

  post: function (url, data, csrfToken) {
    console.log(data.cover);
    return request
      .post(url)
      .set('X-CSRFToken', csrfToken)
      // .type('multipart/form-data')
      .field('name', data.name)
      .field('short_description', data.shortDescription)
      .field('website_url', data.websiteUrl)
      .field('repo_url', data.repoUrl)
      .field('description', data.description)
      .attach('cover', data.cover);
  }
};

module.exports = apiRequests;
