<template>
  <div id='sidebar'>
    <div v-if='$store.getters.activeServer' class='headerWrapper'>
      <h2 class='header'>{{ $store.getters.activeServer.name }}</h2>
      <ToggleServerMenuButton />
    </div>
    <div v-else class='headerWrapper'>
      <h2 class='header'>No Servers Found</h2>
      <AddServerMenuButton />
    </div>

    <div class='serverList' v-if='$store.state.serverListOpen'>
      <ServerSidebarItem
        v-for='server in $store.state.servers'
        v-bind:key='server.id'
        :server='server'
      />
      <AddServerMenuButton
        text='Add New'
        class='addNew' />
    </div>

    <div id="nav">
      <Navigator to="/applications">Applications</Navigator>
      <Navigator to="/clientkeys">Client Keys</Navigator>
      <Navigator to="/">Dashboard</Navigator>
      <Navigator to="/filebrowser">File Browser</Navigator>
      <Navigator to="/monitoring">Monitoring</Navigator>
      <Navigator to="/settings">Settings</Navigator>
      <Navigator to="/Users">Users</Navigator>
    </div>
  </div>
</template>

<script>
import AddServerMenuButton from '@/components/buttons/AddServerMenu.vue'
import Navigator from '@/components/Navigator.vue'
import ServerSidebarItem from '@/components/ServerSidebarItem.vue'
import ToggleServerMenuButton from '@/components/buttons/ToggleServerMenu.vue'

export default {
  components: {
    AddServerMenuButton,
    Navigator,
    ServerSidebarItem,
    ToggleServerMenuButton,
  },
  computed: {
    activeServer() {
      if(!this.$store.state.servers.length) return null
      return this.$store.state.servers.find(server => server.id == this.activeServerId)
    },
    serverCount() {
      return this.$store.state.servers.length
    },
  },
  data() {
    return {
      activeServerId: 25,
      serverListOpen: false,
    }
  },
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
#nav {
  padding: 16px;
  a {
    display: block;
    width: 100%;
    text-align: left;
    font-size: 20px;
    color: $darkblue;
    padding: 8px 0px;
    text-decoration: none;
    outline: 0;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#sidebar {
  border-right: 2px #888 solid;
  box-sizing: border-box;
  height: 100vh;
  width: 320px;
  position: fixed;
  top: 0;
}
.headerWrapper {
  background-color: $darkblue;
  display: flex;
  justify-content: space-between;
  height: 50px;
  width: 100%;
  h2.header {
    box-sizing: border-box;
    color: white;
    text-transform: uppercase;
    text-align: left;
    padding: 16px;
    font-size: 24px;
  }
}
.addNew {
  padding: 0;
  text-align: left;
  width: 100%;
  margin-top: 16px;
}
.serverList {
  background-color: $darkblue;
  border-top: 1px white solid;
  color: white;
  padding: 16px;
}
</style>
