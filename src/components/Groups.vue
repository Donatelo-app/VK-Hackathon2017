<template>
  <div id="groups">
    <nav>
      <div class="nav-wrapper vk-color">
        <p class="flow-text">Ваши привязанные группы:</p>
      </div>
    </nav>
    <div class="container">
      <p class="flow-text center-align">Пока ничего нет, начните работу с <b>DonateLo</b> просто привязав Вашу группу! Это просто!</p>
    </div>
    <a id="add-group" class="btn-floating btn-large waves-effect waves-light vk-color">
      <router-link :to="'create'">
        <i class="material-icons">add</i>
      </router-link>
    </a>
  </div>
</template>

<script>
  module.exports = {

  }
</script>

<style lang="css">
  #add-group {
    position: absolute;
    bottom: 25px;
    right: 25px;
  }
  .nav-wrapper > p {
    margin: 0 25px;
  }
  .label {
    font-size: 2em;
    font-weight: 300;
  }
</style>
