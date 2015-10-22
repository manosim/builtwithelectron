var React = require('react');
var apiRequests = require('../utils/api-requests');

var SubmitForm = React.createClass({

  getInitialState: function () {
    return {
      name: '',
      shortDescription: '',
      websiteUrl: ''
    };
  },

  handleChange: function (key, event) {
    var state = {};
    state[key] = event.target.value;
    this.setState(state);
  },

  submitForm: function (e) {
    e.preventDefault();
    var self = this;

    apiRequests
      .post('http://0.0.0.0:8000/api/directory/submit/', {
        'name': self.state.name,
        'short_description': self.state.shortDescription,
        'website_url': self.state.websiteUrl
      }, this.props.csrfToken)
      .end(function (err, response) {
        if (response && response.ok) {
          // Success - Do Something.
          alert('YES YES!');
        } else {
          // Error - Show messages.
          // Show appropriate message
          alert(err);
        }
      });
  },

  render: function () {
    return (
      <div className='submit-form'>
        <h3>Submition form goes here</h3>
        <form className='form'>
          <input type='text' className='form-control' name='name' onChange={this.handleChange.bind(this, 'name')} />
          <input type='text' className='form-control' name='short_description' onChange={this.handleChange.bind(this, 'shortDescription')} />
          <input type='text' className='form-control' name='website_url' onChange={this.handleChange.bind(this, 'websiteUrl')} />
          <button className='btn btn-primary btn-block' onClick={this.submitForm}>Submit Entry</button>
        </form>
      </div>
    );
  }
});

module.exports = SubmitForm;
