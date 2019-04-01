<template>
  <div class='editServerForm'>
    <div class='field'>
      <label>Server Name: </label>
      <input v-model='server.name' type='text' />
    </div>
    <div class='field'>
      <label>IP Address: </label>
      <input v-model='server.ip_address' type='text' />
    </div>
    <div class='field'>
      <label>Username: </label>
      <input v-model='server.username' type='text' />
    </div>
    <div class='field'>
      <label>Hosting Provider: </label>
      <input v-model='server.hosting_provider' type='text' />
    </div>
    <div class='field'>
      <SaveButton :clickEvent='saveChanges'>Save Changes</SaveButton>
    </div>
  </div>
</template>

<script>
import SaveButton from '@/components/buttons/SaveButton.vue';

export default {
  components: {
    SaveButton,
  },
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
.editServerForm {
  width: 600px;
  .field {
    box-sizing: border-box;
    align-items: center;
    display: flex;
    padding: 8px 0px;

    width: 100%;
    justify-content: space-between;
  }
  label {
    width: 200px;
  }
  input {
    flex-grow: 1;
    padding: 8px;
  }
}
</style>
