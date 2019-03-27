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
  font-size: 24px;
  padding: 16px;
  font-weight: 900;
}


</style>
