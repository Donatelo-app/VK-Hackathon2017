<template>
  <div id="app" style="width: 100vw; overflow-y: auto; overflow-x: hidden;">
    <transition name="slide">
      <router-view></router-view>
    </transition>
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
  .slide-leave-active,
  .slide-enter-active {
    transition: .4s;
  }
  .slide-enter {
    transform: translate(100%, 0);
  }
  .slide-leave-to {
    transform: translate(-100%, 0);
  }
</style>
