const express = require('express')
const next = require('next')
const dotenv = require('dotenv')
const path = require('path')

// Load env variables
dotenv.config({ path: path.resolve(__dirname, '.env') })

const port = parseInt(process.env.PORT, 10) || 3000
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  const server = express()

  // All requests handled by Next.js
  server.use((req, res) => handle(req, res))

  server.listen(port, (err) => {
    if (err) throw err
    console.log(`> Ready on http://localhost:${port}`)
  })
})
