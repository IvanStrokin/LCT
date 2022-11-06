import React from 'react';
import { BrowserRouter, Route,Routes } from 'react-router-dom';
import './App.css'
import Login from "./Components/Login/Login";
import useToken from "./Components/useToken/useToken";
import ExcelPage from "./Components/ExcelRender/ExcelRender";
import "antd/dist/antd.css";
import {Map} from "./Components/Map/Map";

function App() {
    const { token, setToken } = useToken();
    if(!token) {
        return <Login setToken={setToken} />
    }
    return (
        <div>
            <ExcelPage/>
        </div>
    );
    }
export default App;
