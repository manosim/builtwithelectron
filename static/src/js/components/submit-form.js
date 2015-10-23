var _ = require('underscore');
var React = require('react');
var Dropzone = require('react-dropzone');
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
        cover: null,
        tags: []
      },
      success: false,
      errors: false,
      loading: false
    };
  },

  handleChange: function (key, event) {
    var state = {};
    var data = this.state.data;
    data[key] = event.target.value;
    this.setState({
      data: data
    });
  },

  onDrop: function (files) {
    var data = this.state.data;
    data.cover = files[0];
    this.setState({
      data: data
    });
  },

  onOpenClick: function () {
    this.refs.dropzone.open();
  },

  submitForm: function (e) {
    e.preventDefault();
    var self = this;

    this.setState({
      success: false,
      loading: true
    });

    apiRequests
      .post('http://0.0.0.0:8000/api/directory/submit/', this.state.data, this.props.csrfToken)
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
          <div className={this.state.errors['name'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='name'>Application Name</label>
            <input type='text' id='name' className='form-control input-lg' value={this.state.data.name} onChange={this.handleChange.bind(this, 'name')} />
          </div>
          <div className={this.state.errors['short_description'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='shortDescription'>Short Description</label>
            <input type='text' id='shortDescription' className='form-control input-lg' value={this.state.data.shortDescription} onChange={this.handleChange.bind(this, 'shortDescription')} />
          </div>
          <div className={this.state.errors['website_url'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='websiteUrl'>Website Url</label>
            <input type='text' id='websiteUrl' className='form-control input-lg' value={this.state.data.websiteUrl} onChange={this.handleChange.bind(this, 'websiteUrl')} />
          </div>
          <div className={this.state.errors['repo_url'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='repoUrl'>Repository Url</label>
            <input type='text' id='repoUrl' className='form-control input-lg' value={this.state.data.repoUrl} onChange={this.handleChange.bind(this, 'repoUrl')} />
          </div>

          <Dropzone ref='dropzone' className='dropzone' onDrop={this.onDrop} disableClick={true} multiple={false} activeClassName='active'>
            <h4 className='text-center'>drop your awesome image here</h4>
            <a className='btn btn-primary' onClick={this.onOpenClick}>Upload your image</a>
            {this.state.data.cover ? <img className='img-responsive' src={this.state.data.cover.preview} /> : null}
          </Dropzone>

          <div className={this.state.errors['description'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='description'>Description</label>
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
