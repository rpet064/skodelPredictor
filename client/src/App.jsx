import './App.css';
import { useState } from 'react'
import { Navbar, Container, Nav, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouseUser, faAddressCard, faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGithub, faLinkedin } from "@fortawesome/free-brands-svg-icons";
library.add(faHouseUser, faAddressCard, faEnvelope, faGithub, faLinkedin);



export default function App() {
  // show API result after recieving name in form
  const [showForm, setShowForm] = useState(true);
  const [name, setName] = useState("");

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
          <Button id="home-button" title="Home" type="button" onClick={() => setShowForm(true)}>
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
      <div id='container'>
          <div className='card'>
            <h1> Skodel Mood Predictor</h1>
            <h3>Insert your name and it will make a prediction</h3>
            <form onSubmit={handleSubmit}>
          <label>Name: 
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}>
          </input>
          </label>
          <input type="submit" id="form-button"/>
        </form>
        </div>
      </div>:
      <div>
        <h1>These are your results from the API</h1>
      </div>}
      <footer>
      <div>
        <a href="https://github.com/rpet064"><FontAwesomeIcon className="footer-icon" icon={["fab", "github"]} title="Github"/></a>
        <a href="www.linkedin.com/in/robert-pether-ba9968113"><FontAwesomeIcon className="footer-icon" icon={["fab", "linkedin"]} title="Linkedin"/></a>
        <a href="mailto:rpether@hotmail.co.nz"><FontAwesomeIcon className="footer-icon" icon={["fas", "envelope"]} title="Email"/></a>
      </div>
      <p>Copyright Robert Pether {new Date().getFullYear()}</p>
    </footer>
    </div>
  );
}