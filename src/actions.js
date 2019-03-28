import db from './datastore'
import router from './router'

const actions = {
  closeServerList({commit}) {
    commit('closeServerList')
  },
  createNewServer(context, {data}) {
    // Save server to database
    db.insert(data, function(err, doc) {
      context.dispatch('refreshServerListFromDB')
      context.commit('setActiveServerId', doc._id)
    })
  },
  navigate({ commit, state }, destination){
    if(state.serverListOpen) commit('closeServerList')
    router.push(destination)
  },
  initializeServerList({ commit }, servers) {
    commit('saveServersToState', servers)
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
  toggleServerList({ commit }) {
    commit('toggleServerList')
  },
}
export default actions
