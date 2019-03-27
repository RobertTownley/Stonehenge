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
  created() {
    this.$db.find({}, function(err, docs) {
      console.log(err)
      console.log(docs)
    })
  },
}
</script>
