<template>
  <div class='clientKey'>
    <div class='row'>
      <label>Filepath:</label>
      <div>{{ clientKey.filepath }}</div>
    </div>
    <div class='row options'>
      <img
        v-on:click='editClientKey'
        v-bind:src='require("@/assets/icons/pencilDarkBlue.svg")'
      />
      <img
        class='trash'
        v-if='!showDeleteConfirmation'
        v-on:click='deleteClientKey'
        v-bind:src='require("@/assets/icons/trashDarkBlue.svg")'
      />
    </div>
    <div class='deleteConfirmation' v-if='showDeleteConfirmation'>
      <div>Deleting this client key will lock you out of any servers that are using this key. You can "forget" this key to stop tracking it while keeping it in place. Or, if you're sure you want to remove it, you can delete the file permanently.
      </div>
      <div class='deleteOptions'>
        <button v-on:click='cancel' class='safe'>Cancel</button>
        <button v-on:click='forgetKey' class='unsafe'>Forget</button>
        <button v-on:click='deleteKey' class='dangerous'>Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDeleteConfirmation: false,
    }
  },
  methods: {
    deleteClientKey() {
      this.showDeleteConfirmation = true
    },
    editClientKey() {
      console.log("Edit");
    },
    cancel() {
      this.showDeleteConfirmation = false
    },
    forgetKey() {
      console.log("Forget")
    },
    deleteKey() {
      console.log("Delete key")
    },
  },
  props: ['clientKey'],
}
</script>

<style lang='scss' scoped>
@import '@/styles/_colors.scss';
@import '@/styles/_layout.scss';

.clientKey {
  box-sizing: border-box;
  border: 1px $darkblue solid;
  padding: 16px;

  .row {
    align-items: center;
    display: flex;
    justify-content: space-between;
    padding-bottom: 16px;
    &:last-child {
      padding-bottom: 0px;
    }
    &.options {
      padding-top: 32px;
      justify-content: flex-end;
    }

    label {
      font-weight: bold;
      margin-right: 16px;
    }
  }
  img {
    cursor: pointer;
    height: 36px;
    width: 36px;
    padding-left: 16px;
    &.trash {
      width: 28px;
      height: 28px;
    }

  }
}
.deleteConfirmation {
  color: red;
  border: 2px red solid;
  padding: 16px;
  max-width: 50vw;
}
.deleteOptions {
  padding-top: 16px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  button {
    @extend .styledButton;
    background-color: white;
    border: 0;
    font-size: 18px;
    text-transform: uppercase;
    &:hover {
      background-color: white;
      color: $darkblue;
    }
    border-width: 2px;
    border-style: solid;
    &.safe {
      color: $green;
      border-color: $green;
    }
    &.unsafe {
      color: $orangered;
      border-color: $orangered;
    }
    &.dangerous {
      color: red;
      border-color: red;
    }
  }
}
</style>
