const electron = window.require('electron')
const { exec } = electron.remote.app.child_process

export async function getConnectionStatus(server) {
  return new Promise((resolve) => {
    let command = 'uptime'
    let remoteCmd = `ssh ${server.username}@${server.ip_address} ${command}`
    exec(remoteCmd, (err, stdout, stderr) => {
      if(stderr || err) {
        resolve("Connection Failed")
      }
      resolve("Connected")
    })
  })
}
