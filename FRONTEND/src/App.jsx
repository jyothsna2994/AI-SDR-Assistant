import "./App.css";
import { useState } from "react";

function App() {
  const [company, setCompany] = useState("");
  const [website, setWebsite] = useState("");
  const [contact, setContact] = useState("");
  const [designation, setDesignation] = useState("");
  const [result, setResult] = useState(null);

  const generateEmail = async () => {
    const response = await fetch("https://ai-sdr-backend-79iq.onrender.com/company", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        company,
        website,
        contact,
        designation,
      }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="container">
      <h1>AI SDR Assistant</h1>

      <input
        type="text"
        placeholder="Company"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
      />

      <input
        type="text"
        placeholder="Website"
        value={website}
        onChange={(e) => setWebsite(e.target.value)}
      />

      <input
        type="text"
        placeholder="Contact"
        value={contact}
        onChange={(e) => setContact(e.target.value)}
      />

      <input
        type="text"
        placeholder="Designation"
        value={designation}
        onChange={(e) => setDesignation(e.target.value)}
      />

      <button onClick={generateEmail}>
        Generate Email
      </button>

      {result && (
        <div className="result">
          <h2>📧 AI Generated Email</h2>

          <p><strong>Company:</strong> {result.company}</p>
          <p><strong>Contact:</strong> {result.contact}</p>
          <p><strong>Campaign:</strong> {result.campaign}</p>

          <hr />

          <h3>Subject</h3>
          <p>{result.subject}</p>

          <h3>Email</h3>
          <pre>{result.email}</pre>

          <h3>Follow-up Email 1</h3>
          <pre>{result.followup1}</pre>

       <h3>Follow-up Email 2</h3>
      <pre>{result.followup2}</pre>

      <h3>Follow-up Email 3</h3>
      <pre>{result.followup3}</pre>
        </div>
      )}
    </div>
  );
}

export default App;