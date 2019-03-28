<template>
  <div id="app">
    <Sidebar />
    <div id='container'>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  components: {
    Sidebar,
  },
  created() {
    this.$store.dispatch('refreshServerListFromDB')
  },
}
</script>

<style lang="scss">
@import '@/styles/_colors.scss';
@import '@/styles/_reset.scss';
@import '@/styles/_fonts.scss';
#app {
  display: flex;
  font-family: 'Source', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  justify-content: space-between;
}
#container {
  box-sizing: border-box;
  color: $darkblue;
  padding: 0px 16px;
  margin-left: 320px;
  width: 100vw;
  height: 100vh;
}
</style>
