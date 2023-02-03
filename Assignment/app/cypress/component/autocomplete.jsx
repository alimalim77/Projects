import React, {useState, useRef, useEffect} from 'react'


export default function Autocomplete() {
  const nameRef = useRef(null);
  const emailRef = useRef(null);
  const addressRef = useRef(null);

  const [submittedName, setSubmittedName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    setSubmittedName(nameRef.current.value);
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

