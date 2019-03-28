<template>
  <div id='addNewServer'>
    <PageHeader>Add New Server</PageHeader>
    <div class='newServerForm'>
      <div class='formRow'>
        <label for='serverName'>Server Name</label>
        <input name='serverName' v-model='serverName' type='text' />
      </div>
      <div class='formRow'>
        <button v-on:click='submitServerForm'>Create New Server</button>
      </div>
    </div>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'
export default {
  name: 'AddServer',
  components: {
    PageHeader,
  },
  methods: {
    submitServerForm() {
      const data = {
        dateCreated: Date.now(),
        name: this.serverName,
        type: 'server',
      }
      this.$store.dispatch('createServer', data)
    },
  },
}
</script>
