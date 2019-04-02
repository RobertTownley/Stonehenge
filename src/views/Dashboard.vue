<template>
  <div id='dashboard'>
    <PageHeader>Dashboard</PageHeader>
    <ConnectionStatus />
    <div>TODO: Security</div>
    <div>TODO: Server Health</div>
    <div>Stonehenge Version: {{ version }}</div>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader'
import ConnectionStatus from '@/components/ConnectionStatus'
import { version } from '../../package.json'

export default {
  components: {
    ConnectionStatus,
    PageHeader,
  },
  computed: {
    version() {
      return version
    }
  },
  data() {
    return {
    }
  },
  name: 'Dashboard',
}
</script>
