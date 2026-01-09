import { useState } from 'react'
import './App.css'
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

function App() {
  const [show, setShow] = useState(false);
  const [adminMode, setAdminMode] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const wlaczAdministratora = () => setAdminMode(true);
  const wylaczAdministratora = () => setAdminMode(false);

  return (
    <>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Hanalei+Fill&display=swap');
      </style>
      <div className='BodyStyle '>
      <div className="Header">
        <div className="Logo">
          <img src="/logo.png" alt="Logo"/>
        </div>
        <p className="hanalei-fill-regular">Wydarzenia w miescie</p>
        <div className='Info'>
          <p style={{ visibility: adminMode ? 'visible' : 'hidden' }}>Jesteś teraz w trybie Administratora</p>
        </div>
      </div>
      <div className="Lead">
        <p>
          Nasza strona powstała, aby <strong>ułatwić odkrywanie wydarzeń w Twoim mieście</strong> i pomagać w planowaniu wolnego czasu. 
          Dzięki aplikacji szybko sprawdzisz koncerty, festiwale, spotkania i inne atrakcje dostępne w okolicy. 
          To wygodne narzędzie dla mieszkańców oraz osób odwiedzających miasto, które chcą być na bieżąco z lokalnym życiem. 
          Dołącz do nas już teraz i zobacz, że <del>znajdowanie ciekawych wydarzeń jest czasochłonne</del> korzystanie z aplikacji może być proste i przyjemne.
        </p>
      </div>
      <div className="EventsTable">
        <table>
          <thead>
            <tr>
              <th>Nazwa wydarzenia</th>
              <th>Data</th>
              <th>Miejsce</th>
              <th>Godzina rozpoczęcia</th>
              <th>Godzina zakończenia</th>
              <th>Akcje</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>a </td>
              <td>a</td>
              <td>a</td>
              <td>a</td>
              <td>a</td>
              <td><Button variant="primary" onClick={handleShow} className="BtnSzczegoly">Szczegóły</Button></td>
            </tr>
          </tbody>
        </table>
        <Modal
          show={show}
          onHide={handleClose}
          backdrop="static"
          keyboard={false}
        >
        <Modal.Header closeButton>
          <Modal.Title>Modal title</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          I will not close if you click outside me. Do not even try to press
          escape key.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="success" onClick={handleClose}>Understood</Button>
        </Modal.Footer>
      </Modal>
      <Button variant="primary" className='BtnAdmin' style={{visibility: adminMode ? 'hidden' : 'visible'}} onClick={wlaczAdministratora}>Włącz tryb administratora</Button>
      <Button variant="danger" className='BtnAdmin2' style={{visibility: adminMode ? 'visible' : 'hidden'}} onClick={wylaczAdministratora}>Wyłącz tryb administratora</Button>
      </div>
      <div className="Footer">
        <p>
          © 2026 Wydarzenia w Mieście. 
          Wszelkie prawa zastrzeżone. 
          Korzystając z serwisu, akceptujesz obowiązujące warunki użytkowania oraz politykę prywatności. 
          Strona wykorzystuje pliki cookies w celu zapewnienia prawidłowego działania oraz ulepszania jakości usług. 
          Szczegółowe informacje znajdziesz w odpowiednich zakładkach serwisu.
        </p>
      </div>
      </div>
    </>
  )
}

export default App
