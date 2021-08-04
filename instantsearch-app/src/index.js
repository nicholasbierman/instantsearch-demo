import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import configureStore from './store';
import { BrowserRouter } from 'react-router-dom';

const store = configureStore();

window.store = store;

function Root() {
  return (
      <BrowserRouter>
        <App />
      </BrowserRouter>
  );
}

ReactDOM.render(<Root />, document.getElementById('root'));
