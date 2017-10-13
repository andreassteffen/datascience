import React, { Component } from 'react';
import './App.css';
import NameForm from './NameForm';
import { Container, Row, Col, Button } from 'reactstrap';

require('tracking');
require('tracking/build/data/face')

let X = 0;
let Y = 0;
let WIDTH = 0;
let HEIGHT = 0;

class App extends Component {
  constructor(props){
      super(props);
      this.state = {
    }
  }

  tracker = null;

  submit = () => {

  }
    capture =() =>{
      let context = this.refs.screenshot.getContext('2d');
       console.log(X,Y,WIDTH, HEIGHT)
        context.drawImage(this.refs.cameraOutput,  0,0,320,240);
        var img = this.refs.screenshot.toDataURL("image/png");
        fetch('/get_foto', {
          method: 'POST',
          headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
          }, body: JSON.stringify({img: img, x:X, y:Y, width:WIDTH, height:HEIGHT})
      })
    }
  componentDidMount () {
    this.tracker = new window.tracking.ObjectTracker('face')
    this.tracker.setInitialScale(4)
    this.tracker.setStepSize(1)
    this.tracker.setEdgesDensity(0.1)

    window.tracking.track(this.refs.cameraOutput, this.tracker, { camera: true })
    this.tracker.on('track', event => {
      let context = this.refs.canvas.getContext('2d')
      context.clearRect(0, 0, this.refs.cameraOutput.width, this.refs.cameraOutput.height)
      event.data.forEach(function(rect) {
        context.strokeStyle = '#a64ceb'
        context.strokeRect(rect.x,rect.y,rect.width, rect.height);
        X = rect.x;
        Y = rect.y;
        WIDTH = rect.width;
        HEIGHT = rect.height;
      })
    })

  }

  componentWillUnmount () {
    this.tracker.removeAllListeners()
  }

  render () {
    return (
      <div >
          <Row>
              <NameForm className="nameform"/>
          </Row>
          <Row>
              <canvas ref="screenshot" width="320" height="240"></canvas>
          </Row>

          <Row>
            <div >
                <video className="webcam" ref="cameraOutput" width="320" height="240" preload autoPlay loop muted></video>
                <canvas className='plotcanvas' ref="canvas" width="320" height="240"></canvas>
            </div>
          </Row>
          <Row>
              <Button style={{top:'600px', position:'absolute'}} onClick={this.capture}>shoot</Button>

          </Row>



      </div>
    )
  }
}
export default App;

