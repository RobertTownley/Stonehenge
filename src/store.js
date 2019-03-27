import router from './router'
import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
  actions: {
    closeServerList({commit}) {
      commit('closeServerList')
    },
    navigate(context, destination){
      context.dispatch('closeServerList')
      router.push(destination)
    },
    openServerList({commit}) {
      commit('openServerList')
    },
    setServerToActive({ commit }, serverId) {
      commit('closeServerList')
      commit('setActiveServerId', serverId)
    },
    toggleServerList({commit}) {
      commit('toggleServerList')
    },
  },
  getters: {
    activeServer: (state) => {
      if(!state.servers.length) return null
      return state.servers.find(server => server.id === state.activeServerId)
    },
  },
  mutations: {
    closeServerList(state) {
      state.serverListOpen = false;
    },
    openServerList(state) {
      state.serverListOpen = true;
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
    servers: [
      {
        id: 25,
        name: 'Personal Server',
      },
      {
        id: 29,
        name: 'Other Server',
      },
    ],
    serverListOpen: false,
  },
})
