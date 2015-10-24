'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var SubmitForm = require('./components/submit-form');

window.setupSubmitForm = function (csrfToken, tags) {
  ReactDOM.render(<SubmitForm csrfToken={csrfToken} tags={tags} />, document.getElementById('submit-form'));
};
