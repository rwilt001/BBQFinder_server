import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
//import Menu from "./Menu";
//import Home from "./Home";
const App = () => (
  <DataProvider endpoint="menus" 
                render={data => <Table data={data} />} />
);

export default App;