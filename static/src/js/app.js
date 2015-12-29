var $ = window.$ = window.jQuery = require('jquery'); // eslint-disable-line no-unused-vars
var bootstrap = require('bootstrap'); // eslint-disable-line no-unused-vars

var React = require('react'); // eslint-disable-line no-unused-vars
var ReactDOM = require('react-dom');
var SubmitForm = require('./components/submit-form');
var TypedText = require('./components/typed-text');

window.setupSubmitForm = function (csrfToken, tags) {
  ReactDOM.render(
    <SubmitForm csrfToken={csrfToken} tags={tags} />,
  document.getElementById('submit-form'));
};

window.setupTypedText = function () {
  ReactDOM.render(
    <TypedText />,
  document.getElementById('typed-text'));
};
