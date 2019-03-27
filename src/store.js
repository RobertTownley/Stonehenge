import router from './router'
import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
  actions: {
    closeServerList({commit}) {
      commit('closeServerList')
    },
    createNewServer(context, {db, data}) {
      // Save server to database
      db.insert(data, function(err, doc) {
        context.dispatch('refreshServerListFromDB', db)
        context.commit('setActiveServerId', doc._id)
      })
    },
    navigate(context, destination){
      context.dispatch('closeServerList')
      router.push(destination)
    },
    openServerList({commit}) {
      commit('openServerList')
    },
    initializeServerList({ commit }, servers) {
      commit('saveServersToState', servers)
    },
    refreshServerListFromDB({ commit }, $db) {
      $db.find({'type': 'server'}, function(err, servers) {
        commit('saveServersToState', servers)
      })
    },
    setServerToActive({ commit }, serverId) {
      commit('closeServerList')
      commit('setActiveServerId', serverId)
      router.push('/editServer')
    },
    toggleServerList({commit}) {
      commit('toggleServerList')
    },
  },
  getters: {
    activeServer: (state) => {
      if(!state.servers.length) {
        console.log("GETTER FAILED HERE")
        return null
      }
      return state.servers.find(server => {
        console.log("TRYING")
        console.log(server)
        return server.id === state.activeServerId
      })
    },
  },
  mutations: {
    closeServerList(state) {
      state.serverListOpen = false
    },
    openServerList(state) {
      state.serverListOpen = true
    },
    saveServersToState(state, servers) {
      state.servers = servers
    },
    setActiveServerId(state, serverId) {
      state.activeServerId = serverId
    },
    toggleServerList(state) {
      state.serverListOpen = !state.serverListOpen
    },
  },
  state: {
    activeServerId: 25,
    servers: [],
    serverListOpen: false,
  },
})
