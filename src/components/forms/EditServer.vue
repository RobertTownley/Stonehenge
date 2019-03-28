<template>
  <div class='editServerForm'>
    <div class='field'>
      <label>Server Name: </label>
      <input v-model='server.name' type='text' />
    </div>
    <div class='field'>
      <button v-on:click='saveChanges'>Save Changes</button>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    server() {
      return this.$store.getters.activeServer
    }
  },
  methods: {
    saveChanges() {
      this.$store.dispatch('updateActiveServer', this.server)
    }
  },
}
</script>

<style lang='scss' scoped>

</style>
