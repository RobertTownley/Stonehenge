<template>
  <div class='editServerForm'>
    <div class='field'>
      <label>Server Name: </label>
      <input v-model='formData.name' type='text' />
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
  data() {
    return {
      formData: {},
    }
  },
  created() {
    this.formData = this.server
  },
  methods: {
    saveChanges() {
      this.$store.dispatch('updateActiveServer', this.formData)
    }
  },
}
</script>

<style lang='scss' scoped>

</style>
