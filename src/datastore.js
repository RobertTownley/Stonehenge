import Datastore from 'nedb'
import path from 'path'
const electron = window.require('electron')

export default new Datastore({
  autoload: true,
  filename: path.join(electron.remote.app.getPath('userData'), '/data.db')
})
