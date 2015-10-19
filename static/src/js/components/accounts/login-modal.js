var React = require('react');
var ReactDOM = require('react-dom');

var LoginModal = React.createClass({
  getInitialState: function() {
    return {
      loading: false
    };
  },

  componentWillMount: function () {

  },

  render: function() {
    return (
      <div className="login-modal">
        <h1>Okay sport! Now Login ;)</h1>
      </div>
    );
  }
});

module.exports = LoginModal;
