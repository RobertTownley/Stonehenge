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
    this.$store.dispatch('refreshServerListFromDB', this.$db)
  },
}
</script>

<style lang="scss">
@import '@/styles/_reset.scss';
@import '@/styles/_fonts.scss';
#app {
  font-family: 'Source', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  justify-content: space-between;
}
#container {
  box-sizing: border-box;
  padding: 0px 16px;
  margin-left: 320px;
}
</style>
