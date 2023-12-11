const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3001;


const corsOptions = {
    origin: 'http://localhost:3000', // Allow requests from this origin
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true, // Include any other headers you might need
};

app.use(cors(corsOptions));
app.use(bodyParser.json());
app.use('/audio', cors(corsOptions), express.static('C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\outputAudio\\concatenated_audio_output_f.wav'));

  let isAudioReady = false; // Track audio readiness

  app.get('/audio-ready', (req, res) => {
    res.status(isAudioReady ? 200 : 204).end();
  });

  app.post('/generate-audio', (req, res) => {
  const inputText = req.body.text;

  const textFilePath = 'C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\inputText.txt';
  const outputFolderPath = 'C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\outputAudio';
  fs.writeFileSync(textFilePath, '');

    // Clear the output folder
    fs.readdir(outputFolderPath, (err, files) => {
        if (err) throw err;

        for (const file of files) {
            fs.unlink(path.join(outputFolderPath, file), err => {
                if (err) throw err;
            });
        }
    });

    // Write to the text file
    fs.writeFile(textFilePath, inputText, (err) => {
        if (err) {
            console.error(`Error saving text to file: ${err}`);
            return res.status(500).send('Error saving text to file');
        }

  
  // Adjust the path to the actual location of your notebook
  const scriptPath = 'C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\inferences.py';

  // Command to execute inference file
  const command = `python "${scriptPath}" "${textFilePath}"`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error}`);
      return res.status(500).send('Error executing file');
    }
    if (stderr) {
      console.error(`Stderr: ${stderr}`);
    }

    console.log(`Stdout: ${stdout}`);
    isAudioReady = true;
    // Send back a response indicating successful execution
    res.json({ message: 'File executed successfully' });
  });
});
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});