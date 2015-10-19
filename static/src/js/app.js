'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var LoginModal = require('./components/accounts/login-modal');

window.setupLoginModal = function () {
  ReactDOM.render(<LoginModal />, document.getElementById('login-modal'));
};
