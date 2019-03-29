<template>
  <button v-on:click='refreshClientKeys()'>{{ text }}</button>
</template>

<script>
import {
  getPublicKeyFiles,
  savePublicKeysToDB
} from '@/utils/keys';
export default {
  data() {
    return {
      text: 'Refresh Client Keys',
    }
  },
  methods: {
    refreshClientKeys() {
      getPublicKeyFiles()
        .then((keys) => { return savePublicKeysToDB(keys)})
        .then(() => {
          this.$store.dispatch('refreshClientKeysFromDB')
        })
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

