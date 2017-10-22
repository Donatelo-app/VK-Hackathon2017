<template>
  <div id="groups">
    <nav>
      <div class="nav-wrapper vk-color">
        <p class="flow-text">Ваши привязанные группы:</p>
      </div>
    </nav>

    <div class="container">
      <div class="groups" v-if="Object.keys(groups).length">
        <group v-for="(item, key) in groups" :image="item" :gid="key"></group>
      </div>
      <p v-else class="flow-text center-align">Пока ничего нет, начните работу с DonateLo просто привязав Вашу группу! Это просто!</p>
    </div>

    <router-link :to="'info_group'" id="add-group" class="btn-floating btn-large waves-effect waves-light vk-color">
      <i class="material-icons">add</i>
    </router-link>
  </div>
</template>

<script>
  const Group = require('./Group.vue');

  module.exports = {
    components: {
      Group
    },
    computed: {
      groups() {
        return this.$store.state.groups;
      }
    },
    mounted() {
      this.$store.dispatch('loadGroups');
    }
  }
</script>

<style lang="css">
  #add-group {
    position: fixed;
    bottom: 25px;
    right: 25px;
  }
  .nav-wrapper > p {
    margin: 0 25px;
  }
  .container {
    margin-top: 50px;
  }
</style>
