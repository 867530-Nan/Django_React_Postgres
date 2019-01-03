import React from "react";
import axios from "axios";
import { FilePond } from "react-filepond";
import "filepond/dist/filepond.min.css";

class Home extends React.Component {
  state = { files: null, text: "" };

  handleSubmit = () => {
    console.log("baby steps");
    axios
      .post("http://127.0.0.1:8000/fileupload/")
      .then(res => console.log("the response" + res));
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

  render() {
    return (
      <div>
        <h1>Home Component</h1>
        <FilePond
          allowMultiple={true}
          onupdatefiles={fileItems => {
            this.setState({
              files: fileItems.map(fileItem => fileItem.file)
            });
          }}
        />
        <hr />
        <input
          type="text"
          placeholder="Enter Text Here.."
          value={this.state.text}
          onChange={e => this.setState({ text: e.target.value })}
        />
        {this.state.files !== null || this.state.text !== ""
          ? this.displaySubmit()
          : null}
      </div>
    );
  }
}
export default Home;
