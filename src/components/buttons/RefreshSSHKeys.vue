<template>
  <button v-on:click='refreshClientKeys()'>{{ text }}</button>
</template>

<script>
export default {
  data() {
    return {
      text: 'Refresh Client Keys',
    }
  },
  methods: {
    refreshClientKeys() {
      alert("Refreshing");
    }
  }
}
</script>

<style lang='scss' scoped>
@import '@/styles/_layout.scss';
button {
  @extend .styledButton;
}
</style>

