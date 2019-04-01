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
    this.$store.dispatch('initializeStateFromDB')
  },
}
</script>

<style lang="scss">
@import '@/styles/_colors.scss';
@import '@/styles/_reset.scss';
@import '@/styles/_fonts.scss';
@import '@/styles/_layout.scss';

#app {
  display: flex;
  font-family: 'Source', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
p {
  line-height: 1.4;
  font-size: 16px;
  max-width: 800px;
}
h1, h2, h3 {
  margin-bottom: 16px;
}
h1 {
  font-size: 36px;
}
h2 {
  font-size: 32px;
}
h3 {
  font-size: 28px;
}
</style>
