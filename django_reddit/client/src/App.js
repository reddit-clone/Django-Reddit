import React, { Component } from 'react';
import './App.css';
import {BrowserRouter as Router, Route, Switch, Link} from "react-router-dom";
import Home from './components/Home'
import PostShow from './components/PostShow'
import UserShow from './components/UserShow'
import CommentShow from './components/CommentShow'
class App extends Component {
  render() {
    return (
      <Router>
                <div className="App">

                    <div>
                        <h1>Tunr</h1>
                        <div>
                            <div><Link to="/">All Artists</Link></div>
                        </div>
                    </div>

                    <Switch>
                      <Route exact path="/" component={Home}/>
                      <Route path="/post/:postid" component={PostShow}/>
                      <Route path="/user/:userid" component={UserShow}/>
                      <Route path="/post/:postid/comment/:commentid" component={CommentShow} />
                    </Switch>
                </div>
            </Router>
    );
  }
}

export default App;
