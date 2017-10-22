<template>
  <div id="app" style="width:720px; height:580px; overflow-y: auto; overflow-x: hidden;">
    <router-view></router-view>
    <preload v-show="load"></preload>
  </div>
</template>

<script>
  const Preload = require('./Preload.vue');
  module.exports = {
    components: {
      Preload
    },
    computed: {
      load() {
        return this.$store.state.load;
      }
    }
  }
</script>
<style>
  body {
    overflow-x: hidden;
    background: #dfe3e6;
  }
  .vk-color {
    background: #5e81a8 !important;
  }
</style>
