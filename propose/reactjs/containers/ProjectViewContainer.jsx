import React from 'react';
import Modal from 'react-modal';
import PropTypes from 'prop-types';
import { Grid, Row, Col } from 'react-flexbox-grid';
import { Form, TextareaField, SubmitField } from 'react-components-form';
import Schema from 'form-schema-validation';
import Cookies from 'js-cookie';

import Navbar from '../components/Navbar';

const applyProjectSchema = new Schema({
  message: {
    login: String,
    required: true
  }
})

export default class ProjectViewContainer extends React.Component {
  static propTypes = {
    projectsId: PropTypes.number,
  }

  constructor(props) {
    super(props)
    this.state = {project: {}, user: {},modalIsOpen: false}
  }

  componentDidMount() {
    let component = this
    console.log('In component did mount', component.props)
    let url = "/api/projects/" + component.props.projectId.toString();

    let settings = {
        method: "GET",
        credentials: 'same-origin'
    };

    fetch(url, settings)
        .then((response) => response.json())
        .then((data) => {
          console.log(data, "Looking at data")
          component.setState({project:data});
        });

    const userUrl = "/api/profile/"
    fetch(userUrl, settings)
      .then((response) => response.json())
      .then((data) => {
        console.log(data, "looking at user data")
        component.setState({user:data})
      })
  }

  _renderSkills = (project) => {
    if (!project.tags) {
      return <span/>;
    }
    const skills = project.tags.map(tag => {
      return <li>{tag.name}</li>
    })
    return (
      <ul>
        {skills}
      </ul>
    )
  }

  _renderButtons = () => {
    if (this.state.user && this.state.project.client && this.state.user.id !== this.state.project.client.id) {
      return (
        <div className="buttons">
          <button className="btn btn-secondary" onClick={this.openModel}>
            Save
          </button>
          <button className="btn btn-primary" onClick={this.openModel}>
            Apply
          </button>
        </div>
        )
    }

    return (
      <div className="buttons">
        <button className="btn btn-secondary" onClick={this.openModel}>
          Remove
        </button>
        <a href={"/projects/" + this.state.project.id +"/edit"}>
        <button className="btn btn-primary">
          Edit
        </button>
        </a>
        <a href={"/applicants/" + this.state.project.id +"/"}>
        <button className="btn btn-secondary" onClick={this.openModel}>
          Applicants
        </button>
        </a>
      </div>
      )
  }

  openModel = () => {
    this.setState({modalIsOpen: true})
  }

  closeModal = () => {
    this.setState({modalIsOpen: false})
  }

  onSubmit = (model) => {
    var headers = new Headers();

    headers.append('Accept', 'application/json'); // This one is enough for GET requests
    headers.append('Content-Type', 'application/json'); // This one sends body
    headers.append('X-CSRFToken', Cookies.get("csrftoken"))
    const applyUrl = "/api/applications/";
    const details = {
      details: {
        project: this.state.project.id,
        freelancer: this.state.user.id,
        client: this.state.project.client.id,
        message: model.message,
      }
    }
    const settings = {
        method: "POST",
        credentials: 'same-origin',
        headers: headers,
        body: JSON.stringify(details)
    };
    fetch(applyUrl,  settings)
        .then((response) => response.json())
        .then((data) => {})
    alert('Applied!');
    this.setState({modalIsOpen: false});
    window.location.replace('/applications/')
  }

  render() {
    let clientName = "";
    if (this.state.project && this.state.project.client && this.state.project.client.user) {
      clientName = this.state.project.client.user.first_name + " " + this.state.project.client.user.last_name;
    }

    let modalStyle = {
      overlay: {
        backgroundColor: 'rgba(0, 0, 0, 0.7)'
      },
      content: {
        margin: '0 auto',
        marginTop: '50px',
        backgroundColor: '#FFFFFF',
        height: '500px',
        width: '700px',
      }
    }

    return (
      <div className="project-view">
        <Navbar />
        <Grid fluid>
          <Row>
            <Col xs={5}>
              <h1>{this.state.project.title}</h1>
              <h5>{`by ${clientName}`}</h5>
              <h4>Project Summary</h4>
              {this.state.project.description}
            </Col>
            <Col xs={3}>
              {this._renderButtons()}
            </Col>
            <Col xs={4}>
              <h3>Similar Projects</h3>
              <h3>Skills</h3>
              {this._renderSkills(this.state.project)}
            </Col>
          </Row>
        </Grid>
        <Modal
          isOpen={this.state.modalIsOpen}
          onAfterOpen={() => {}}
          onRequestClose={this.closeModal}
          contentLabel="Application Form"
          ariaHideApp={false}
          style={modalStyle}
        >
          <h3>Project Application</h3>
          <div className="form">
            <Form
              onSubmit={this.onSubmit}
              onError={(errors, model) => console.log('error', errors, model)}
            >
              <TextareaField className="textarea" name="message" label="Message" />
              <SubmitField value="Apply" />
            </Form>
          </div>
        </Modal>
      </div>
    )
  }
}
