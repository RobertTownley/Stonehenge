<template>
  <button v-on:click='toggleMenu()'>
    <img src='@/assets/icons/hamburgerWhite.svg'/>
  </button>
</template>

<script>
export default {
  props: ['toggleMenu']
}

</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
button {
  background-color: $darkblue;
  border: 0;
  outline: 0;
  width: 60px;
}
img {
  height: 100%;
}
</style>
