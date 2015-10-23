var _ = require('underscore');
var React = require('react');
var apiRequests = require('../utils/api-requests');

var SubmitForm = React.createClass({

  getInitialState: function () {
    var date = new Date();
    var now = date.getTime();

    return {
      data: {
        name: 'Test ' + now,
        shortDescription: 'Example',
        websiteUrl: 'http://www.example.com/',
        repoUrl: 'http://www.anotherexample.com/repo',
        description: 'Full description here..',
        tags: []
      },
      success: false,
      errors: false,
      loading: false
    };
  },

  handleChange: function (key, event) {
    var state = {};
    state.data[key] = event.target.value;
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
        'name': self.state.data.name,
        'short_description': self.state.data.shortDescription,
        'website_url': self.state.data.websiteUrl,
        'repo_url': self.state.data.repoUrl,
        'description': self.state.data.description,
        'tags': self.state.data.tags
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
        {this.state.success ? <h1>SUBMITTED SPORT :)</h1> : null}
        <form className='form'>
          <div className='form-group'>
            <label for='name'>Application Name</label>
            <input type='text' id='name' className='form-control input-lg' value={this.state.data.name} onChange={this.handleChange.bind(this, 'name')} />
          </div>
          <div className='form-group'>
            <label for='shortDescription'>Short Description</label>
            <input type='text' id='shortDescription' className='form-control input-lg' value={this.state.data.shortDescription} onChange={this.handleChange.bind(this, 'shortDescription')} />
          </div>
          <div className='form-group'>
            <label for='websiteUrl'>Website Url</label>
            <input type='text' id='websiteUrl' className='form-control input-lg' value={this.state.data.websiteUrl} onChange={this.handleChange.bind(this, 'websiteUrl')} />
          </div>
          <div className='form-group'>
            <label for='repoUrl'>Repository Url</label>
            <input type='text' id='repoUrl' className='form-control input-lg' value={this.state.data.repoUrl} onChange={this.handleChange.bind(this, 'repoUrl')} />
          </div>
          <div className='form-group'>
            <label for='description'>Description</label>
            <textarea className='form-control input-lg' id='description' rows='4' value={this.state.data.description} onChange={this.handleChange.bind(this, 'description')}></textarea>
          </div>

          <div>{JSON.stringify(this.state.errors)}</div>
          <button className='btn btn-primary btn-lg btn-block' onClick={this.submitForm}>Submit Entry</button>
        </form>
      </div>
    );
  }
});

module.exports = SubmitForm;
