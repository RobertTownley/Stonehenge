<template>
  <div id='dashboard'>
    <PageHeader>Dashboard</PageHeader>
    <ConnectionStatus />
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader'
import ConnectionStatus from '@/components/ConnectionStatus'

export default {
  name: 'Dashboard',
  components: {
    ConnectionStatus,
    PageHeader,
  },
  data() {
    return {
    }
  },
}
</script>
