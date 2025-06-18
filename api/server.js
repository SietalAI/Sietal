const express = require('express');
const app = express();
const agentRoutes = require('./agentRoutes');
const auth = require('./auth');

app.use(auth);
app.use('/api', agentRoutes);

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

