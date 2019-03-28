<template>
  <div id='settings'>
    <PageHeader class='settingsHeader'>Settings</PageHeader>
    <EditServerForm v-if='$store.getters.activeServer' />
  </div>
</template>

<script>
import EditServerForm from '@/components/forms/EditServer.vue'
import PageHeader from '@/components/PageHeader.vue'

export default {
  name: 'Settings',
  components: {
    EditServerForm,
    PageHeader,
  }
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
#settings {
  color: $darkblue;
  font-size: 20px;
  text-align: left;
}
.settingsHeader {
  padding-left: 0;
}
</style>
