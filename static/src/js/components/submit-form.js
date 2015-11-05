var _ = require('underscore');
var capitalize = require("underscore.string/capitalize");
var React = require('react');
var Select = require('react-select');
var Dropzone = require('react-dropzone');
var apiRequests = require('../utils/api-requests');

var Autogenerator = require('./autogenerator');

var SubmitForm = React.createClass({

  getInitialState: function () {
    return {
      data: {
        name: '',
        shortDescription: '',
        websiteUrl: '',
        repoUrl: '',
        description: '',
        cover: null,
        tags: []
      },
      tags: [],
      selectedTags: [],
      success: false,
      errors: false,
      loading: false,
      submitDisabled: false
    };
  },

  componentWillMount: function() {
    var flattenTags = [];
    var tagsJson = JSON.parse(this.props.tags);
     _.map(tagsJson, function (tag) {
      flattenTags.push({
        value: tag.pk,
        label: tag.fields.name
      });
    });
    this.setState({
      tags: flattenTags
    });
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

  onClearCover: function () {
    var data = this.state.data;
    data['cover'] = null;
    this.setState({
      data: data
    });
  },

  tagRenderer: function (option) {
    return <span key={option.pk}>{option.label}</span>
  },

  tagValue: function (option) {
		return <strong>{option.label}</strong>;
	},

  tagsSelected: function (val, selectedOptions) {
    var selectedTags = [];

    _.each(selectedOptions, function (tag) {
      selectedTags.push(tag.value);
    });

    var data = this.state.data;
    data.tags = selectedTags;

    this.setState({
      data: data,
      selectedTags: selectedOptions
    });
  },

  submitForm: function (e) {
    e.preventDefault();
    var self = this;

    this.setState({
      success: false,
      loading: true,
      submitDisabled: true
    });

    apiRequests
      .post('/api/directory/submit/', this.state.data, this.props.csrfToken)
      .end(function (err, response) {
        if (response && response.ok) {
          self.setState({
            success: true,
            errors: [],
            loading: false,
            submitDisabled: false
          });
        } else {
          self.setState({
            errors: response.body,
            loading: false,
            submitDisabled: false
          });
        }
      });
  },

  populateForm: function (args) {
    var data = this.state.data;
    data.name = capitalize(args.name);
    data.shortDescription = args.description ? args.description : '';
    data.websiteUrl = args.homepage ? args.homepage : '';
    data.repoUrl = args.html_url ? args.html_url : '';
    this.setState({
      data: data
    });
  },

  renderFieldErrors: function (field) {
    if (this.state.errors[field]) {
      return (
        <div className='help-block'>
          {_.map(this.state.errors[field], function (obj, key) {
            return <div key={key}>{obj}</div>;
          })}
        </div>
      );
    }
  },

  render: function () {
    return (
      <div className='submit-form'>
        <Autogenerator gotDetails={this.populateForm} />

        <form className='form'>
          <div className={this.state.errors['name'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='name' className='control-label'>Application Name <span className='required'>*</span></label>
            <input type='text' id='name' className='form-control input-lg' value={this.state.data.name} onChange={this.handleChange.bind(this, 'name')} />
            {this.renderFieldErrors('name')}
          </div>
          <div className={this.state.errors['short_description'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='shortDescription' className='control-label'>Short Description <span className='required'>*</span></label>
            <input type='text' id='shortDescription' className='form-control input-lg' value={this.state.data.shortDescription} onChange={this.handleChange.bind(this, 'shortDescription')} />
            {this.renderFieldErrors('short_description')}
          </div>
          <div className={this.state.errors['website_url'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='websiteUrl' className='control-label'>Website Url</label>
            <input type='text' id='websiteUrl' className='form-control input-lg' value={this.state.data.websiteUrl} onChange={this.handleChange.bind(this, 'websiteUrl')} />
            {this.renderFieldErrors('website_url')}
          </div>
          <div className={this.state.errors['repo_url'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='repoUrl'>Repository Url</label>
            <input type='text' id='repoUrl' className='form-control input-lg' value={this.state.data.repoUrl} onChange={this.handleChange.bind(this, 'repoUrl')} />
            {this.renderFieldErrors('repo_url')}
          </div>

          <label>Tags</label>
          <Select
            name="form-field-name"
            value={this.state.selectedTags}
            options={this.state.tags}
            onChange={this.tagsSelected}
            optionRenderer={this.tagRenderer}
            valueRenderer={this.tagValue}
            multi={true}
            placeholder='Enter your tags' />

          <label>Photo/Screenshot</label>
          <Dropzone ref='dropzone' className='dropzone' onDrop={this.onDrop} disableClick={true} multiple={false} activeClassName='active'>
            {this.state.data.cover ? (
              <div>
                <i className='fa fa-check-circle' />
                <div className='filename'>{this.state.data.cover.name}</div>
                <small className='clear' onClick={this.onClearCover}>Clear</small>
              </div>) : (
              <div>
                <h4 className='text-center'>drop your awesome image here</h4>
                <a className='btn btn-primary' onClick={this.onOpenClick}>Upload your image</a>
              </div>
            )}
          </Dropzone>

          {this.state.errors.cover ? (
            <div className='alert alert-danger'>{this.state.errors.cover[0]}</div>
          ) : null}

          <div className={this.state.errors['description'] ? 'form-group has-error' : 'form-group'}>
            <label htmlFor='description'>Description</label>
            <textarea className='form-control input-lg' id='description' rows='4' value={this.state.data.description} onChange={this.handleChange.bind(this, 'description')}></textarea>
            {this.renderFieldErrors('description')}
          </div>

          {this.state.success ? (
            <div className='alert alert-success'>Submiited successfully! You will receive an email once it gets approved.</div>
          ): null}

          {_.isEmpty(this.state.errors) ? null : (
            <div className='alert alert-danger'>Oops! Please complete all the required fields and submit your applications.</div>
          )}
          <button className='btn btn-primary btn-lg btn-block' disabled={this.state.submitDisabled} onClick={this.submitForm}>Submit Entry</button>
        </form>
      </div>
    );
  }
});

module.exports = SubmitForm;
