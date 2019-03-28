<template>
  <div id='settings'>
    <PageHeader>Settings</PageHeader>
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
