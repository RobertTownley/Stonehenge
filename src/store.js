import router from './router'
import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
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
  mutations: {
    closeServerList(state) {
      state.serverListOpen = false;
    },
    openServerList(state) {
      state.serverListOpen = true;
    },
    toggleServerList(state) {
      state.serverListOpen = !state.serverListOpen
    },
  },
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
    toggleServerList({commit}) {
      commit('toggleServerList')
    },
  }
})
