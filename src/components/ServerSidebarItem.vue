<template>
  <div
    :class='isActive ? "server active" : "server inactive"'
    v-on:click='$store.dispatch("setServerToActive", server.id)'
  >
    {{ server.name }}
  </div>
</template>

<script>
export default {
  computed: {
    isActive() {
      return this.$store.state.activeServerId === this.server.id
    },
  },
  props: ['server'],
}
</script>

<style lang='scss' scoped>
.server {
  cursor: pointer;
  font-size: 20px;
  padding: 8px 0px;
  text-align: left;
  &.active {
    font-weight: bold;
  }
}
</style>
