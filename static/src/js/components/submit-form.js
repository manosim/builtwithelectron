var _ = require('underscore');
var React = require('react');
var apiRequests = require('../utils/api-requests');

var SubmitForm = React.createClass({

  getInitialState: function () {
    var date = new Date();
    var now = date.getTime();

    return {
      name: 'Test ' + now,
      shortDescription: 'Example',
      websiteUrl: 'http://www.example.com/',
      tags: [],
      success: false,
      errors: false,
      loading: false
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

    this.setState({
      loading: true
    });

    apiRequests
      .post('http://0.0.0.0:8000/api/directory/submit/', {
        'name': self.state.name,
        'short_description': self.state.shortDescription,
        'website_url': self.state.websiteUrl,
        'tags': self.state.tags
      }, this.props.csrfToken)
      .end(function (err, response) {
        if (response && response.ok) {
          self.setState({
            success: true,
            errors: [],
            loading: false
          });
        } else {
          self.setState({
            errors: response.body,
            loading: false
          });
        }
      });
  },

  render: function () {
    return (
      <div className='submit-form'>
        <h3>Submition form goes here</h3>
        {this.state.success ? <h1>SUBMITTED SPORT :)</h1> : null}
        <form className='form'>
          <input type='text' className='form-control' value={this.state.name} onChange={this.handleChange.bind(this, 'name')} />
          <input type='text' className='form-control' value={this.state.shortDescription} onChange={this.handleChange.bind(this, 'shortDescription')} />
          <input type='text' className='form-control' value={this.state.websiteUrl} onChange={this.handleChange.bind(this, 'websiteUrl')} />
          <div>{JSON.stringify(this.state.errors)}</div>
          <button className='btn btn-primary btn-block' onClick={this.submitForm}>Submit Entry</button>
        </form>
      </div>
    );
  }
});

module.exports = SubmitForm;
