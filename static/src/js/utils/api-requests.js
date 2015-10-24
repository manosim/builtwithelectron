var request = require('superagent');

var apiRequests = {
  get: function (url) {
    return request
      .get(url)
      .set('Accept', 'application/json');
  },

  post: function (url, data, csrfToken) {
    return request
      .post(url)
      .set('X-CSRFToken', csrfToken)
      .field('name', data.name)
      .field('short_description', data.shortDescription)
      .field('website_url', data.websiteUrl)
      .field('repo_url', data.repoUrl)
      .field('description', data.description)
      .field('tags', data.tags)
      .attach('cover', data.cover, 'cover.png');
  }
};

module.exports = apiRequests;
