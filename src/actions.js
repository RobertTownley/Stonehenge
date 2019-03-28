import db from './datastore'
import router from './router'

const actions = {
  // Database Operations
  createServer(context, data) {
    db.insert(data, function(err, doc) {
      context.dispatch('refreshServerListFromDB')
      context.commit('setActiveServerId', doc._id)
    })
  },
  updateActiveServer({ commit, state }, data) {
    db.update(
      {_id: state.activeServerId},
      {$set: data},
      {},
      function(){
        db.find({'type': 'server'})
          .sort({order: 1})
          .exec(function(err, servers){
            commit('saveServersToState', servers)
          })
      })
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
  setServerToActive({ commit }, serverId){
    commit('setActiveServerId', serverId)
  },
  toggleServerList({ commit }) {
    commit('toggleServerList')
  },
}
export default actions
