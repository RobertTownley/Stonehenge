<template>
  <button v-on:click='clickEvent'><slot></slot></button>
</template>

<script>
export default {
  data() {
    return {
      'classThing': 'Here',
    }
  },
  props: ['clickEvent'],
}
</script>

<style lang='scss' scoped>
@import '@/styles/_layout.scss';
button {
  @extend .styledButton;
}
</style>

