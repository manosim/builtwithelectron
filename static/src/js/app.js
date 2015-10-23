'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var SubmitForm = require('./components/submit-form');

window.setupSubmitForm = function (csrfToken) {
  ReactDOM.render(<SubmitForm csrfToken={csrfToken} />, document.getElementById('submit-form'));
};
