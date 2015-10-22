var React = require('react');

var SubmitForm = React.createClass({

  getInitialState: function () {
    return {
      example: ''
    };
  },

  render: function () {
    return (
      <div className='submit-form'>
        <h3>Submition form goes here</h3>
      </div>
    );
  }
});

module.exports = SubmitForm;
