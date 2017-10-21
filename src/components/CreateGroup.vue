<template>
  <div id="create-group">
    <form @submit.prevent="createGroup">

      <div id="add-wallpaper">
        <div id="preview-image" :style="{backgroundImage: 'url(' + image + ')'}"></div>
        <input type="file" id="select-image" @change="onFileChange" required>
        <i class="material-icons add-photo-icon">add_a_photo</i>
        <br>
        <p class="flow-text">Загрузите обложку группы</p>
      </div>

      <div class="container">
        <div class="row">
          <p class="flow-text">Укажите данные группы:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="gid" v-model="groupId" type="text" required class="validate">
              <label for="gid">ID группы</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input id="token" v-model="tokenGroup"  type="text" required class="validate">
              <label for="token">Токен группу</label>
            </div>
          </div>

          <p class="flow-text">Ваши реквезиты:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="bitcoin" v-model="bitcoinWallet"  type="text" required class="validate">
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
        this.$store.dispatch('uploadData', {
          gid: this.groupId,
          info: {
            cover: {
              background: this.image,
              views: []
            },
            wallets: {
              token: this.tokenGroup,
              bitcoin: this.bitcoin,
              mastercard: this.mastercard,
              tinkoff: this.tinkoff,
              qiwi: this.tinkoff
            }
          }
        });
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
    height: 300px;
    border: 5px dashed #7a9ee0;
    width: 100%;
    text-align: center;
    padding-top: 110px;
    position: relative;
    box-sizing: border-box;
  }
  #add-wallpaper i, #add-wallpaper p {
    color: #7a9ee0;
    margin-top: 0;
    text-align: center;
  }
  #preview-image {
    position: absolute;
    width: 100vw;
    height: 300px;
    background-position: center;
    background-size: cover;
    z-index: 100;
    top: -5px;
    left: -5px;
  }
  #select-image {
    cursor: pointer;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
  }

  .add-photo-icon {
    font-size: 3em;
  }
</style>
