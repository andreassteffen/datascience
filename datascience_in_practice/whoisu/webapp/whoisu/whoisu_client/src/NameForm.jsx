import React from 'react';
import { Col, Form, FormGroup, Label, Input } from 'reactstrap';

export default class NameForm extends React.Component {
  render() {
    return (
      <Form>
        <FormGroup row>
          <Label for="firstname" sm={2} size="lg">first name</Label>
          <Col sm={10}>
            <Input type="text" name="firstname" id="firstname" placeholder="first name" size="lg" />
          </Col>
        </FormGroup>
        <FormGroup row>
          <Label for="name" sm={2}>name</Label>
          <Col sm={10}>
            <Input type="text" name="name" id="name" placeholder="name" />
          </Col>
        </FormGroup>
      </Form>
    );
  }
}