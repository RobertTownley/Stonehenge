<template>
  <div class='serverList'>
    <div v-if='serverCount === 0' class='header'>No Servers Found</div>
    <div v-else class='header'>My Servers</div>
  </div>
</template>

<script>
export default {
  computed: {
    serverCount() {
      return this.servers.length
    },
  },
  data() {
    return {
      servers: [1,2],
    }
  }
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
.header {
  background-color: $darkblue;
  color: white;
  text-transform: uppercase;
  text-align: left;
  padding: 16px;
  font-size: 24px;
}
</style>
