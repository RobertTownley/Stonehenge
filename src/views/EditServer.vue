<template>
  <div id='editServer'>
    <PageHeader>{{ server.name }} Settings</PageHeader>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'

export default {
  name: 'Configure Server',
  components: {
    PageHeader,
  },
  computed: {
    server() {
      return this.$store.getters.activeServer
    }
  },
}
</script>
