<template>
  <div class="card">
      <router-link :to="{path: 'edit', query: {gid}}">
        <div class="card-image waves-effect">
          <img :src="'data:image/png;base64,' + image">
        </div>
      </router-link>
      <div class="card-content">
        <span class="card-title activator grey-text text-darken-4">OXXXYMIRON OFFICIAL
          <i class="material-icons right waves-effect" id="remove" @click="removeGroup">close</i>
        </span>
      </div>
  </div>
</template>

<script>
  module.exports = {
    props: ['image', 'gid'],
    methods: {
      removeGroup() {
        this.$store.dispatch('removeGroup', {gid: this.gid});
      }
    }
  }
</script>

<style lang="css">
  #remove {
    z-index: 10000;
  }
  .card {
    box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14);
  }
</style>
