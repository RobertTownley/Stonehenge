const electron = require('electron');
const app = electron.app
const BrowserWindow = electron.BrowserWindow

app.child_process = require('child_process')
app.on('ready', () => {
  let win = new BrowserWindow({width: 800, height: 600})
  const url = process.env.NODE_ENV === 'DEV'
    ? `http://localhost:8080`
    : `file://${__dirname}/dist/index.html`
  win.loadURL(url)
})
