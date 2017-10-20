<template>
  <div id="groups">
    <div class="container">
      <h1 class="label">Ваши привязанные группы:</h1>
      <div class="valign-wrapper">
        <p class="flow-text center-align">Пока ничего нет, начните работу с <b>DonateLo</b> просто привязав Вашу группу! Это просто!</p>
      </div>
    </div>
    <a id="add-group" class="btn-floating btn-large waves-effect waves-light blue darken-3"><i class="material-icons">add</i></a>
  </div>
</template>

<script>
  module.exports = {

  }
</script>

<style lang="css">
  #groups {
    height: 100vh;
  }
  #add-group {
    position: absolute;
    bottom: 25px;
    right: 25px;
  }
  .label {
    font-size: 2em;
    font-weight: 300;
  }
  .container, .valign-wrapper {
    height: 100%;
  }
</style>
