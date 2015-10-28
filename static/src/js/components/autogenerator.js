var _ = require('underscore');
var React = require('react');
var Select = require('react-select');
var Dropzone = require('react-dropzone');
var apiRequests = require('../utils/api-requests');

var Autogenerator =  require('./autogenerator');

var SubmitForm = React.createClass({

  getInitialState: function () {
    return {
      url: 'http://www.github.com/ekonstantinidis/gitify',
      submitDisabled: false,
      loading: false
    };
  },

  handleChange: function (key, event) {
    this.setState({
      url: event.target.value
    });
  },

  onSubmit: function () {
		console.log('Making the request...');
    var self = this;
    var slug = this.state.url.split('.com/')[1];
    var owner = slug.split('/')[0];
    var repo = slug.split('/')[1];
    console.log(owner, '/', repo);

    this.setState({
      submitDisabled: true
    });

    apiRequests
      .get('https://api.github.com/repos/' + owner + '/' + repo)
      .end(function (err, response) {
        if (response && response.ok) {
          self.setState({
            success: true,
            errors: [],
            loading: false,
            submitDisabled: false
          });
          self.props.gotDetails(response.body);
        } else {
          self.setState({
            errors: response.body,
            loading: false,
            submitDisabled: false
          });
        }
      });
  },

  render: function () {
    return (
      <div className='autogenerator'>
        <h3>Open-Source Populator</h3>
        <form className='form'>
          <div className='form-group'>
            <input type='text' id='name' className='form-control input-lg' value={this.state.url} onChange={this.handleChange.bind(this, 'url')} />
          </div>
          {this.state.errors ? (
            <div className='alert alert-danger'>Oops! Something went wrong and we could not auto-populate the form.</div>
          ) : null}
          <button className='btn btn-primary btn-lg btn-block' disabled={this.state.submitDisabled} onClick={this.onSubmit}>Populate Submision Form</button>
         </form>
      </div>
    );
  }
});

module.exports = SubmitForm;
