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

  handleImageChange: function (e) {
    var file = e.target.files[0];
    var data = this.state.data;
    data['cover'] = file;

    this.setState({
      data: data
    });
  },

  // onDrop: function (files) {
  //   var data = this.state.data;
  //   data.cover = files[0];
  //   this.setState({
  //     data: data
  //   });
  //   console.log('Received file: ', this.state.data.cover);
  // },

  submitForm: function (e) {
    e.preventDefault();
    var self = this;

    this.setState({
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
    // <Dropzone className='dropzone' onDrop={this.onDrop} multiple={false}>
    //   <div className='message'>Drop your <strong>awesome</strong> image here</div>
    //   <a className='btn btn-primary'>Upload your image</a>
    //   {this.state.data.cover ? <img className='img-responsive' src={this.state.data.cover.preview} /> : null}
    // </Dropzone>

    return (
      <div className='submit-form'>
        {this.state.success ? <h1>SUBMITTED SPORT :)</h1> : null}
        <form className='form'>
          <div className='form-group'>
            <label htmlFor='name'>Application Name</label>
            <input type='text' id='name' className='form-control input-lg' value={this.state.data.name} onChange={this.handleChange.bind(this, 'name')} />
          </div>
          <div className='form-group'>
            <label htmlFor='shortDescription'>Short Description</label>
            <input type='text' id='shortDescription' className='form-control input-lg' value={this.state.data.shortDescription} onChange={this.handleChange.bind(this, 'shortDescription')} />
          </div>
          <div className='form-group'>
            <label htmlFor='websiteUrl'>Website Url</label>
            <input type='text' id='websiteUrl' className='form-control input-lg' value={this.state.data.websiteUrl} onChange={this.handleChange.bind(this, 'websiteUrl')} />
          </div>
          <div className='form-group'>
            <label htmlFor='repoUrl'>Repository Url</label>
            <input type='text' name='repoUrl' className='form-control input-lg' value={this.state.data.repoUrl} onChange={this.handleChange.bind(this, 'repoUrl')} />
          </div>

          <input type="file" name="somename" size="chars" onChange={this.handleImageChange} />

          <div className='form-group'>
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
