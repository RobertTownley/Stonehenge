import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'


Vue.use(Vuex)

export default new Vuex.Store({
  actions,
  getters: {
    activeServer: (state) => {
      if(!state.servers.length) return null
      return state.servers.find(server => {
        return server._id === state.activeServerId
      })
    },
  },
  mutations: {
    closeServerList(state) {
      state.serverListOpen = false
    },
    saveClientKeysToState(state, keys) {
      state.clientKeys = keys
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
    activeServerId: null,
    clientKeys: [],
    servers: [],
    serverListOpen: false,
  },
})
