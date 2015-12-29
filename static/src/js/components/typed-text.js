var React = require('react');
var malarkey = require('malarkey');

var TypedText = React.createClass({

  componentDidMount: function() {
    var elem = document.querySelector('.typed');
    var opts = {
      typeSpeed: 50,
      deleteSpeed: 50,
      pauseDelay: 1000,
      loop: true,
      postfix: ''
    };
    malarkey(elem, opts)
      .type('Atom').pause().delete()
      .type('Slack').pause().delete()
      .type('GitHub Desktop').pause().delete()
      .type('Visual Studio').pause().delete();
  },

  render: function () {
    return (
      <h2 className='typed-text'>
        <div className='typed-text-content'>
          <span className='typed' />
          <span className='cursor'>|</span>
        </div>
        is made with Electron.
      </h2>
    );
  }
});

module.exports = TypedText;
