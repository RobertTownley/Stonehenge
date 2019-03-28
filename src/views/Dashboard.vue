<template>
  <div id='dashboard'>
    <PageHeader>Dashboard</PageHeader>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue';

export default {
  name: 'Dashboard',
  components: {
    PageHeader,
  },
  data() {
    return {
      test: 'Nothing yet',
    }
  },
}
</script>
