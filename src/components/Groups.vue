<template>
  <div id="groups">
    <nav>
      <div class="nav-wrapper vk-color">
        <p class="flow-text">Ваши привязанные группы:</p>
      </div>
    </nav>

    <div class="container">
      <div class="groups" v-if="isShowGroups">
        <group v-for="(item, key) in groups" :image="item" :gid="key"></group>
      </div>
      <p v-else class="flow-text center-align">Пока ничего нет, начните работу с <b>DonateLo</b> просто привязав Вашу группу! Это просто!</p>
    </div>

    <a id="add-group" class="btn-floating btn-large waves-effect waves-light vk-color">
      <router-link :to="'create'">
        <i class="material-icons">add</i>
      </router-link>
    </a>
  </div>
</template>

<script>
  const Group = require('./Group.vue');

  module.exports = {
    components: {
      Group
    },
    computed: {
      isShowGroups() {
        return !!Object.keys(this.$store.state.groups).length;
      },
      groups() {
        return this.$store.state.groups;
      }
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
