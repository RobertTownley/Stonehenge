<template>
  <button v-on:click='navigateToAddServerView()'>
    <img src='@/assets/icons/addNewWhite.svg'/>
  </button>
</template>

<script>
export default {
  props: ['isOpen'],
  methods: {
    navigateToAddServerView() {
      this.$router.push('/addServer');
    },
  },
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
button {
  background-color: $darkblue;
  border: 0;
  cursor: pointer;
  outline: 0;
  width: 60px;
}
img {
  height: 100%;
  width: 100%;
}
</style>
