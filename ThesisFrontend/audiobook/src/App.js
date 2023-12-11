import React, { useState, useRef } from 'react';
import './App.css'; // Import the custom styles
import Background from './background.svg';

const App = () => {
  const [text, setText] = useState('');
  const [audioSrc, setAudioSrc] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const audioRef = useRef(null);


  const handleConvert = async () => {
    setIsLoading(true);
    setError(null);
    setAudioSrc(null); // Reset the audio source

    try {

      console.log("POSTING")

      const response = await fetch('http://localhost:3001/generate-audio', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
           
        },
        body: JSON.stringify({ text }), // Make sure 'text' is a variable with the text you want to send
      });
      console.log("POSTED")
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      // Wait for the audio to be ready
      let audioReady = false;
      await new Promise(resolve => setTimeout(resolve, 5000));

      // Try for 10 times every 2 seconds
      for (let attempt = 1; attempt <= 200; attempt++) {
        try {
          const audioReadyResponse = await fetch('http://localhost:3001/audio', {
            method: 'HEAD' // HEAD request is sufficient to check if the file exists
          });

          // Check if the audio file is available
          if (audioReadyResponse.ok) {
            audioReady = true;
            console.log('Audio is ready');
            break;
          } else {
            console.log(`Attempt ${attempt}: Audio not ready, retrying...`);
          }
        } catch (error) {
          console.error('Error checking audio readiness:', error);
        }

        // Wait for 2 seconds before the next attempt
        await new Promise(resolve => setTimeout(resolve, 2000));
      }

      if (audioReady) {
        // Now that audio is ready, fetch it
        const audioResponse = await fetch('http://localhost:3001/audio', {
          method: 'GET',
        });
        if (audioResponse.ok) {
          const audioData = await audioResponse.blob();
          const audioUrl = URL.createObjectURL(audioData);
          setAudioSrc(audioUrl);
        } else {
          throw new Error('Audio file not found');
        }
      } else {
        throw new Error('Audio not ready');
      }
    } catch (error) {
      console.error('Error:', error);
      setError(`Error: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handlePlay = () => {
    if (audioRef.current) {
      audioRef.current.play().catch(err => {
        console.error('Error playing audio:', err);
        setError('Error playing audio');
      });
    }
  };

  return (
    <div className="app-container" style={{ backgroundImage: `url(${Background})`, backgroundSize: 'cover', position: 'fixed', minWidth: '100%', minHeight: '100%' }}>
      <header className="header">
        <div className="logo-container">
          {/* Replace the logo URL with your own */}
          <img src="\analyze-sound-wave-iconw.svg" alt="Logo" className="logo" />
        </div>
        <button className="explore-github-button">
          Our Github
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            className="svg-icon"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            />
          </svg>
        </button>
      </header>
      <div className="content-wrapper">
        <div className="content-container">
          <h1 className="app-title">TTS Audiobook Generator</h1>
          <p className="app-description">Experience audiobooks like never before with our audiobook generator! Immerse yourself in emotion-rich narration that brings stories to life</p>

          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter your book text here..."
            className="text-input"
          />

<button onClick={handleConvert} className="convert-button" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Generate'}
          </button>
          {error && <div className="error-message">{error}</div>}
          {audioSrc && (
        <div className="audio-container">
          {/* Using audioRef here */}
          <audio ref={audioRef} src={audioSrc} controls className="audio-player" />
        </div>
      )}
        </div>
      </div>
    </div>
  );
};

export default App;