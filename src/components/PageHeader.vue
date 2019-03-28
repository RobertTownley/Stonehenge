<template>
  <h1 class='pageTitle'><slot></slot></h1>
</template>

<script>
export default{
  props: ['title'],
}
</script>

<style lang='scss' scoped>
.pageTitle {
  padding: 16px 16px 16px 0px;
}


</style>
