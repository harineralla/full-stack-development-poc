import logo from './logo.svg';
import './App.css';
import Time from './components/time';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
          <Time />
      </header>
    </div>
  );
}

export default App;
