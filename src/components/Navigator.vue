<template>
  <a v-on:click='navigate()'><slot></slot></a>
</template>

<script>
export default {
  methods: {
    navigate() {
      this.$store.dispatch('navigate', this.to);
    }
  },
  props: ['to'],
}
</script>

<style lang='scss' scoped>
a {
  cursor: pointer;
}
</style>
