import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';

function Root() {
  return (
      <BrowserRouter>
        <App />
      </BrowserRouter>
  );
}

ReactDOM.render(<Root />, document.getElementById('root'));
