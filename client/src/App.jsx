import './App.css';
import { useState } from 'react'
import { Navbar, Container, Nav, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouseUser, faAddressCard } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
library.add(faHouseUser, faAddressCard);



function App() {
  // show API result after recieving name in form
  const [showForm, setShowForm] = useState(true);
  const [name, setName] = useState("");
  const [about, showAbout] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`The name you entered was: ${name}`)
    setShowForm(false);
  }
  return (
    <div className="App">
      {/* navbar component */}
      <Navbar className="nav" expand="lg">
        <Container>
          <Button title="Home" type="button" onClick={() => setShowForm(true)}>
            SMP
          </Button>
            <Nav className="ms-auto" activeKey="/home">
            <div className='btn-group'>
              <div>
                  <Button title="About this app" id="address-card" type="button" >
                    <a href="https://challenge.parkside-interactive.com/docs/">
                      <FontAwesomeIcon icon={["fas", "address-card"]} />
                    </a>
                  </Button>
                </div>
                <div>
                  <Button title="Home" type="button" onClick={() => setShowForm(true)}>
                    <FontAwesomeIcon icon={["fas", "house-user"]} />
                  </Button>
                </div>
              </div>
            </Nav>
        </Container>
      </Navbar>
        {(showForm)?
      <div>
        <h1>Welome to Skodel Mood Predictor</h1>
        <h3>Insert your name and the app will make a prediction</h3>
        <form onSubmit={handleSubmit}>
          <label>Enter your name:
            <input 
              type="text" 
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </label>
          <input type="submit" />
        </form>
      </div>:
      <div>
        <h1>These are your results from the API</h1>
      </div>}
    </div>
  );
}

export default App;
