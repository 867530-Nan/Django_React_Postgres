import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./Home";
import SingleItem from "./SingleItem";

class App extends Component {
  render() {
    return (
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/:id" component={SingleItem} />
      </Switch>
    );
  }
}

export default App;
