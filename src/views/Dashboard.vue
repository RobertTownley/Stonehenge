<template>
  <div id='dashboard'>
    <PageHeader>Dashboard</PageHeader>
  </div>
</template>

<script>
import db from '@/datastore'
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
  created() {
    db.find({}, function(err, docs) {
      // Do something with docs?
    })
  },
}
</script>
