<template>
  <div id='sidebar'>
    <ServerList />
    <Navigation />
  </div>
</template>

<script>
import ServerList from '@/components/ServerList'
import Navigation from '@/components/Navigation'

export default {
  components: {
    Navigation,
    ServerList,
  }
}
</script>

<style lang='scss'>
#sidebar {
  border-right: 2px #888 solid;
  box-sizing: border-box;
  height: 100vh;
  width: 320px;
  position: fixed;
  top: 0;
}
</style>
