'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var SubmitForm = require('./components/submit-form');

window.setupSubmitForm = function () {
  ReactDOM.render(<SubmitForm />, document.getElementById('submit-form'));
};
