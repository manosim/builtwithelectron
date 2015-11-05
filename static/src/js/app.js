'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var SubmitForm = require('./components/submit-form');
var TypedText = require('./components/typed-text');

window.setupSubmitForm = function (csrfToken, tags) {
  ReactDOM.render(<SubmitForm csrfToken={csrfToken} tags={tags} />, document.getElementById('submit-form'));
};

window.setupTypedText = function () {
  ReactDOM.render(<TypedText />, document.getElementById('typed-text'));
};
