import { useState } from 'react'
import ReactMarkdown from "react-markdown";

interface FormData {
  query: string;
  filename: string;
}

function App() {
  const [formData, setFormData] = useState<FormData>({ query: '', filename: '' });
  const [result, setResult] = useState('');

  function handleInputChange(event: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  }

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const response = await fetch("http://localhost:8000/query",{method: "POST",headers: { 'Content-Type': 'application/json',}, body:JSON.stringify(formData)});
    var result = await response.json();
    result = result['result'];
    setResult(result);
  }
  return (
    <>

      <div className="card">
      <form onSubmit={handleSubmit}>
      <label>
        Query:
        <input type="text" name="query" value={formData.query} onChange={handleInputChange} />
      </label>
      <br />
      <label>
        Filename:
        <input type="text" name="filename" value={formData.filename} onChange={handleInputChange} />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
      </div>
      <div className="result">
      <ReactMarkdown children={result} />
      </div>
    </>
  )
}

export default App
