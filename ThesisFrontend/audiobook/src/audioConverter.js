// const { spawn } = require('child_process');
// const path = require('path');

// const createAudioFile = (text) => {
//   return new Promise((resolve, reject) => {
//     const scriptPath = 'C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\inference.py';

//     const process = spawn('python', [scriptPath, text]);

//     process.stdout.on('data', (data) => {
//       console.log(`stdout: ${data}`);
//     });

//     process.stderr.on('data', (data) => {
//       console.error(`stderr: ${data}`);
//       reject(data.toString());
//     });

//     process.on('close', (code) => {
//       if (code !== 0) {
//         reject(`Process exited with code ${code}`);
//       } else {
//         // Resolve with the path of the generated audio file
//         resolve('C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\src\\concatenated_audio_output.wav');
//       }
//     });
//   });
// };

// module.exports = { createAudioFile };
