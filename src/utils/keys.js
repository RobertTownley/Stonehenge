import path from 'path';
const fs = window.require('fs');
const electron = window.require('electron')

import db from '@/datastore'
const sshDir = path.join(electron.remote.app.getPath('home'), '.ssh')

export async function getPublicKeyFiles() {
  fs.readdir(sshDir, function(err, files){
    return files
  })


  return new Promise(resolve => {
    const keys = fs.readdirSync(sshDir)
    resolve(keys.filter(key => key.indexOf('.pub') >= 0))
  })
}

export async function savePublicKeysToDB(filenames){
  return new Promise(function(resolve){
    let keys = []
    filenames.map(filename => {
      let data = {
        filepath: path.join(sshDir, filename),
        type: 'clientkey',
      }
      keys.push(data)
      db.update(
        {filepath: data.filepath},
        {$set: data},
        {upsert:true})
    })
    resolve(keys)
  });
}
