var _ = require('underscore');
var React = require('react');
var malarkey = require('malarkey');

var TypedText = React.createClass({

  componentDidMount: function() {
    var elem = document.querySelector('.typed-text');
    var opts = {
      typeSpeed: 50,
      deleteSpeed: 50,
      pauseDelay: 2000,
      loop: true,
      postfix: ''
    };
    malarkey(elem, opts).type('Say hello')   .pause().delete()
                        .type('Wave goodbye').pause().delete();
  },

  render: function () {
    return (
      <div className='typed-text'></div>
    );
  }
});

module.exports = TypedText;
