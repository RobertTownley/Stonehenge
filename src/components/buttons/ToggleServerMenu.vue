<template>
  <button v-on:click='toggleMenu()'>
    <img v-if='$store.state.serverListOpen' src='@/assets/icons/closeWhite.svg'/>
    <img v-else src='@/assets/icons/hamburgerWhite.svg'/>
  </button>
</template>

<script>
export default {
  methods: {
    toggleMenu() {
      this.$store.dispatch('toggleServerList');
    },
  }
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
button {
  background-color: $darkblue;
  border: 0;
  cursor: pointer;
  outline: 0;
  width: 60px;
}
img {
  height: 100%;
}
</style>
