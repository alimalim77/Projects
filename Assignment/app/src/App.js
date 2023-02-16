import logo from './logo.svg';
import './App.css';
import React, {useState, useRef, useEffect} from 'react'




function FormWithFocus() {
  const nameRef = ____(null);
  const emailRef = ____(null);
  const addressRef = ____(null);

  const [submittedName, setSubmittedName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // setSubmittedName(nameRef.current.value);
    console.log(`Name: ${nameRef.current.value}`);

  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label style={{ marginBottom: '1rem' }}>
          Name: 
          <input ref={nameRef} type="text" />
        </label>
        <label style={{ marginBottom: '1rem' }}>
          Email:
          <input ref={emailRef} type="email" />
        </label>
        <label style={{ marginBottom: '1rem' }}>
          Address:
          <input ref={addressRef} type="text" />
        </label>
        <input type="submit" value="Submit" />
      </form>
      {submittedName !== '' && (
        <p style={{ marginTop: '1rem' }}>
          Submitted name: {submittedName}
        </p>
      )}
    </div>
  );
}

export default FormWithFocus;








