var React = require('react');
var ReactDOM = require('react-dom');
var Modal = require('react-bootstrap').Modal;

const customStyles = {
  content : {
    overflow: 'hidden'
  }
};


var LoginModal = React.createClass({
  getInitialState: function() {
    return {
      showModal: true
    };
  },

  componentWillMount: function () {

  },

  toggleModal: function () {
    this.setState({showModal: !this.state.showModal});
  },

  handleSaveClicked: function (argument) {
    console.log('Saved!');
  },

  render: function() {
    var modal;

    if (this.state.showModal) {
      modal = (
        <div className="login-modal">
          <Modal.Dialog onHide={this.toggleModal}>
            <Modal.Header>
              <Modal.Title>Login with GitHub</Modal.Title>
            </Modal.Header>

            <Modal.Body>
              <p className='lead'>One fine body...</p>
            </Modal.Body>

            <Modal.Footer>
              <button className="btn btn-default" onClick={this.toggleModal}>Close</button>
              <button className="btn btn-primary">Save changes</button>
            </Modal.Footer>
          </Modal.Dialog>
        </div>
      );
    }

    return (
      <li>
        <a href="#">Login with GitHub</a>
        {modal}
      </li>
    );
  }
});

module.exports = LoginModal;
