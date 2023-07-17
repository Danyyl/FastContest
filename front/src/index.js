import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { Provider, useSelector } from 'react-redux';
import {BrowserRouter} from "react-router-dom";
import configureStore from './store'

const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
        <BrowserRouter>
            <Provider store={configureStore()}>
                <App />
            </Provider>
        </BrowserRouter>
);

