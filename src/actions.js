import db from './datastore'
import router from './router'

import { getConnectionStatus } from '@/utils/connections'

const actions = {
  // Database Operations
  createServer(context, data) {
    db.insert(data, function(err, doc) {
      context.dispatch('refreshServerListFromDB')
      context.commit('setActiveServerId', doc._id)
    })
  },
  updateActiveServer({ commit, dispatch, state }, data) {
    db.update(
      {_id: state.activeServerId},
      {$set: data},
      {},
      function(){
        db.find({'type': 'server'})
          .sort({order: 1})
          .exec(function(err, servers){
            commit('saveServersToState', servers)
            dispatch('navigate', '/')
          })
      })
  },
  refreshClientKeysFromDB(context) {
    db
      .find({type: 'clientkey'})
      .sort({order: 1})
      .exec(function(err, keys){
        context.commit('saveClientKeysToState', keys)
      })
  },
  initializeStateFromDB({ dispatch }) {
    dispatch('refreshServerListFromDB')
    dispatch('refreshClientKeysFromDB')
  },
  refreshServerListFromDB({ commit }) {
    db
      .find({type: 'server'})
      .sort({order: 1})
      .exec(function(err, servers) {
        commit('saveServersToState', servers)
        if(servers.length){
          commit('setActiveServerId', servers[0]['_id'])
        }
      })
  },
  deleteServer(context, serverId) {
    db.remove({_id: serverId})
  },
  
  // UI operations
  closeServerList({commit}) {
    commit('closeServerList')
  },
  navigate({ commit, state }, destination){
    if(state.serverListOpen) commit('closeServerList')
    router.push(destination)
  },
  initializeServerList({ commit }, servers) {
    commit('saveServersToState', servers)
  },
  setServerToActive({ commit, dispatch }, _id){
    commit('setActiveServerId', _id)
    commit('closeServerList')
    dispatch('navigate', '/')
  },
  toggleServerList({ commit }) {
    commit('toggleServerList')
  },

  // Server Interactions
  pingActiveServer({ commit, getters }) {
    if(!getters.activeServer) return null
    getConnectionStatus(getters.activeServer)
      .then(connectionStatus => commit("setConnectionStatus", connectionStatus))
      .catch(err => console.log(err))
  },
  resetConnectionStatus({ commit }) {
    commit('setConnectionStatus', 'Checking...')
  },
}
export default actions
