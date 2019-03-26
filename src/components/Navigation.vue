<template>
  <div id="nav">
    <router-link to="/applications">Applications</router-link>
    <router-link to="/dashboard">Dashboard</router-link>
    <router-link to="/monitoring">Monitoring</router-link>
    <router-link to="/settings">Settings</router-link>
    <router-link to="/Users">Users</router-link>
  </div>
</template>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
#nav {
  padding: 16px;
  a {
    display: block;
    width: 100%;
    text-align: left;
    font-size: 20px;
    color: $darkblue;
    padding: 8px 0px;
    text-decoration: none;
    outline: 0;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
