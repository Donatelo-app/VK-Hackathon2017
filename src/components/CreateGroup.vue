<template>
  <div id="create-group">
    <form @submit.prevent="createGroup">

      <div id="add-wallpaper">
        <div id="preview-image" :style="{backgroundImage: 'url(' + image + ')'}"></div>
        <input type="file" id="select-image" @change="onFileChange" required>
        <p class="flow-text">Загрузите обложку группы</p>
      </div>

      <div class="container">
        <div class="row">
          <p class="flow-text">Укажите данные группы:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="gid" type="text" required class="validate">
              <label for="gid">ID группы</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input id="token" type="text" required class="validate">
              <label for="token">Токен группу</label>
            </div>
          </div>

          <p class="flow-text">Ваши реквезиты:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="bitcoin" type="text" required class="validate">
              <label for="token">Биткоин кошелек</label>
            </div>
          </div>
          <button type="submit" class="col s12 waves-effect waves-light btn btn-large vk-color"><i class="material-icons left">navigate_next</i>Перейти к редактированию</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  module.exports = {
    data() {
      return {
        image: '',
        tokenGroup: '',
        groupId: '',
        bitcoinWallet: ''
      }
    },
    methods: {
      createGroup() {
        this.$store.dispatch('loadGroupData', {
          bg: this.image,
          acess_token: this.tokenGroup,
          gid: this.groupId,
          bitcoin_wallet: this.bitcoinWallet
        });
        this.$router.push('edit');
      },
      onFileChange(e) {
        var files = e.target.files || e.dataTransfer.files;
        if(!files.length) return;

        var reader = new FileReader();
        reader.onload = (e) => {
          this.image = e.target.result;
        };
        reader.readAsDataURL(files[0]);
      }
    }
  }
</script>

<style scoped>
  #add-wallpaper {
    cursor: pointer;
    height: 200px;
    border: 5px dashed #7a9ee0;
    width: 100%;
    text-align: center;
    padding-top: 67px;
    position: relative;
    box-sizing: border-box;
  }
  #preview-image {
    position: absolute;
    width: 100vw;
    height: 200px;
    background-position: center;
    background-size: cover;
    z-index: 100;
    top: -5px;
    left: -5px;
  }
  #select-image {
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
  }
</style>
