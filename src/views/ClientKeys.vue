<template>
  <div id='clientKeys'>
    <PageHeader>Client Keys</PageHeader>
    <div class='wrapper'>
      <div class='keyList' v-if='keys.length'>
        <SSHKeyTile :key='key' v-for='key in keys'/>
      </div>
      <div v-else class='warning'>
        <h3>No client keys found</h3>
        <p>Stonehenge has no record of any client keys on this computer. You can check for existing keys by clicking the
        "Refresh" button, or create a new one by clicking "Generate New Key"</p>
      </div>
      <div class='info'>
        <p>Client keys (also called "SSH keys") are files that allow you to authenticate with servers. Think of them as long passwords that you keep in a file.</p>
        <p>On this page, you can keep track of all of the client keys on your computer. You can generate new client keys, or remove existing ones.</p>
        <p>Keep in mind that removing existing keys locks you out of the server, so only
        delete them if you're sure you don't need them anymore.</p>
      </div>
    </div>
    <div class='keyButtonContainer'>
      <NewSSHKeyButton />
      <RefreshSSHKeysButton />
    </div>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader';
import RefreshSSHKeysButton from '@/components/buttons/RefreshSSHKeys';
import NewSSHKeyButton from '@/components/buttons/NewSSHKey';
import SSHKeyTile from '@/components/SSHKeyTile';

export default {
  name: 'ClientKeys',
  components: {
    NewSSHKeyButton,
    PageHeader,
    RefreshSSHKeysButton,
    SSHKeyTile,
  },
  data() {
    return {
      keys: [],
    }
  }
}
</script>

<style lang='scss' scoped>
#clientKeys {
  text-align: left;
  .wrapper {
    display: flex;
    justify-content: space-between;
  }
  .info {
    padding: 0px 16px;
    width: 300px;
    p {
      margin-bottom: 16px;
    }
  }
  .keyButtonContainer {
    button {
      margin-right: 8px;
    }
  }
}

</style>
