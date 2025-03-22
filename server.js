const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from the public folder
app.use(express.static(path.join(__dirname, 'public')));

// Homepage route (optional, defaults to index.html in /public)
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'home.html'));
});

// Fake call API (already present)
app.get('/fake-call', (req, res) => {
  res.json({
    caller: "John Doe",
    number: "+1234567890",
    message: "Incoming fake call!"
  });
});

// Optional: Dummy routes for Blog, Services, Market pages
app.get('/blog', (req, res) => {
  res.send('<h1>Blog Page Coming Soon!</h1>');
});

app.get('/services', (req, res) => {
  res.send('<h1>Services Page Coming Soon!</h1>');
});

app.get('/market', (req, res) => {
  res.send('<h1>Market Page Coming Soon!</h1>');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
