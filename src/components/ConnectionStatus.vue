<template>
  <div class='statusBar'>
    <div class='connectionStatus'>Connection Status: 
      <span v-bind:class='connectionClass + " connection"'>
        {{ this.$store.state.connectionStatus }}
      </span>
    </div>
    <button
      v-if='this.$store.state.connectionStatus != "Checking..."'
      v-on:click='checkConnectionStatus()'>Refresh</button>
  </div>
</template>

<script>
export default {
  beforeDestroy() {
    clearInterval(this.connectionInterval)
  },
  computed: {
    connectionClass() {
      const conn = this.$store.state.connectionStatus
      if(conn === 'Connected') {
        return 'connected'
      } else if(conn === 'Connection Failed') {
        return 'disconnected'
      } else {
        return 'pending'
      }
    }
  },
  created() {
    setTimeout(this.checkConnectionStatus, 1000)
  },
  methods: {
    checkConnectionStatus() {
      this.$store.dispatch('resetConnectionStatus')
      this.$store.dispatch('pingActiveServer')
      this.connectionInterval = setInterval(() => {
        this.$store.dispatch('resetConnectionStatus')
        this.$store.dispatch('pingActiveServer')
      }, this.$store.state.connectionRefreshInterval)
    },
  },
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
@import '@/styles/_layout.scss';

.connection {
  font-weight: 700;
  &.connected {
    color: $green;
  }
  &.pending {
    color: $orangered;
  }
  &.disconnected {
    color: red;
  }
}
.statusBar {
  box-sizing: border-box;
  align-items: center;
  display: flex;
  justify-content: space-between;
  font-size: 20px;
  border-bottom: 1px $darkblue solid;
  padding: 16px 0px;

  button {
    @extend .styledButton;
    padding: 16px;
  }
}
.connectionStatus {
  border: 1px $darkblue solid;
  padding: 16px;
}

</style>
