import React from "react";
import axios from "axios";
import { FilePond } from "react-filepond";
import "filepond/dist/filepond.min.css";
import { Cookies, withCookies } from "react-cookie";

class Home extends React.Component {
  state = { title: null, text: "", list: [] };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/api/word/")
      .then(res => this.setState({ list: res.data }));
  }

  handleSubmit = () => {
    console.log("baby steps");
    axios
      .post("http://127.0.0.1:8000/api/words/", {
        vector: 1,
        token: this.state.text,
        frequency: 1.1
      })
      .then(res =>
        this.setState({ list: [...this.state.list, res.data], text: "" })
      );
  };

  displaySubmit = () => {
    return (
      <div
        style={{ height: "100px", width: "100px", backgroundColor: "orange" }}
        onClick={this.handleSubmit}
      >
        Submit the thing
      </div>
    );
  };

  displayList = () => {
    return this.state.list.map(single => {
      return <h4>{single.token}</h4>;
    });
  };

  render() {
    return (
      <div>
        <h1>What's been typed..</h1>
        {this.displayList()}
        <hr />
        <hr />
        <hr />
        <h1>Type something in.. </h1>
        <input
          type="text"
          placeholder="Enter Text Here.."
          value={this.state.text}
          onChange={e => this.setState({ text: e.target.value })}
        />
        {this.state.text !== "" ? this.displaySubmit() : null}
      </div>
    );
  }
}
export default withCookies(Home);
