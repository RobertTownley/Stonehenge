<template>
  <div id='dashboard'>
    <PageHeader>Dashboard</PageHeader>
    <div>{{ test }}</div>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue';
const electron = window.require('electron')

export default {
  name: 'Dashboard',
  components: {
    PageHeader,
  },
  computed: {
    test() {
      console.log(electron.remote)
      const test = electron.remote.app.getPath('userData')
      return test
    },
  },
}
</script>
