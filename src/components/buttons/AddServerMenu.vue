<template>
  <button
    v-on:click='$store.dispatch("navigate", "/addServer")'
    :class='text ? "withText" : "withoutText"'
    
  >
    <img src='@/assets/icons/addNewWhite.svg'/>
    <div>{{ text }}</div>
  </button>
</template>

<script>
export default {
  props: ['text'],
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
button {
  background-color: $darkblue;
  border: 0;
  box-sizing: border-box;
  cursor: pointer;
  outline: 0;
  display: flex;
  justify-content: left;
  align-items: center;
  padding: 0px 8px;
  &.withoutText {
    width: 50px;
  }
}
img {
  height: 100%;
  width: 100%;
}
div {
  color: white;
  font-size: 20px;
  width: 100px;
  padding-left: 8px;
  flex: 1;
}
</style>
