<template>
  <div id='sidebar'>
    <div v-if='activeServer' class='headerWrapper'>
      <div class='header'>{{ activeServer.name }}</div>
      <ToggleServerMenuButton :toggleMenu='toggleMenu'/>
    </div>
    <div v-else class='headerWrapper'>
      <div class='header'>No Servers Found</div>
      <AddServerMenuButton />
    </div>

    <div class='serverList' v-if='serverListOpen && serverCount > 1'>
      <div v-for='(server, index) in servers' v-bind:key='index' >
        {{ server.name }}
      </div>
    </div>

    <div id="nav">
      <router-link to="/applications">Applications</router-link>
      <router-link to="/dashboard">Dashboard</router-link>
      <router-link to="/monitoring">Monitoring</router-link>
      <router-link to="/settings">Settings</router-link>
      <router-link to="/Users">Users</router-link>
    </div>
  </div>
</template>

<script>
import AddServerMenuButton from '@/components/buttons/AddServerMenu.vue'
import ToggleServerMenuButton from '@/components/buttons/ToggleServerMenu.vue'

export default {
  components: {
    AddServerMenuButton,
    ToggleServerMenuButton,
  },
  computed: {
    activeServer() {
      return this.servers.length ? this.servers[0] : null
    },
    serverCount() {
      return this.servers.length
    },
  },
  data() {
    return {
      serverListOpen: false,
      servers: [],
      otherThing: [
        {name: 'Personal Server'},
        {name: 'Other Server'},
      ],
    }
  },
  methods: {
    navigate(page) {
      this.$router.push(page);
    },
    toggleMenu() {
      this.serverListOpen = !this.serverListOpen;
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
  .header {
    color: white;
    text-transform: uppercase;
    text-align: left;
    padding: 16px;
    font-size: 24px;
  }
}
</style>
