<template>
  <div id="create-group">
    <nav>
      <div class="nav-wrapper vk-color">
        <div class="row">
          <div class="col s1" style="text-align: center;">
            <router-link :to="'groups'"><i class="material-icons">apps</i></router-link>
          </div>
          <div class="col s11">
            <p class="flow-text" style="margin: 0;">Базовая информация о группе:</p>
          </div>
        </div>
      </div>
    </nav>

    <form @submit.prevent="createGroup">
      <div id="add-wallpaper">
        <div id="preview-image" :style="{backgroundImage: getUrlImage}"></div>
        <input type="file" id="select-image" @change="onFileChange">
        <i class="material-icons add-photo-icon">add_a_photo</i>
        <br>
        <p class="flow-text">Загрузите обложку группы</p>
      </div>

      <div class="container">
        <div class="row">
          <p class="flow-text">Укажите данные группы:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="gid" v-model="groupId" :disabled="isBlockEditGroupId" type="text" required class="validate">
              <label class="active" for="gid">ID группы</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input id="token" v-model="tokenGroup"  type="text" required class="validate">
              <label class="active" for="token">Токен группу</label>
            </div>
          </div>

          <p class="flow-text">Ваши реквезиты:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="bitcoin" v-model="bitcoinWallet"  type="text" class="validate">
              <label class="active" for="token">Биткоин кошелек</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input id="tinkoff" v-model="tinkoffWallet"  type="text" class="validate">
              <label class="active" for="token">Тинькофф банк</label>
            </div>
          </div>
          <p class="flow-text">Сумма сбора:</p>
          <div class="row">
            <div class="input-field col s12">
              <input id="total" v-model="total"  type="number" required class="validate">
              <label class="active" for="total">Рублей:</label>
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
        gid: this.$route.query.gid,
        groupId: '',
        bitcoinWallet: '',
        tinkoffWallet: '',
        total: 50000
      }
    },
    computed: {
      getUrlImage() {
        return 'url(' + this.image + ')';
      }
    },
    methods: {
      createGroup() {
        this.$store.dispatch('uploadData', {
          gid: this.groupId,
          info: {
            token: this.tokenGroup,
            cover: {
              total: this.total,
              background: this.image,
              views: []
            },
            wallets: {
              bitcoin: this.bitcoinWallet,
              tinkoff: this.tinkoffWallet,
            }
          }
        });
        this.$router.push('edit?gid=' + this.gid);
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
    },
    mounted() {
      if(this.$route.query.gid) {
        let group = this.$store.state.group;
        this.image = 'data:image/png;base64,' + group.cover.background;
        $('#preview-image').css('backgroundImage', this.getUrlImage);
        this.tokenGroup = group.token;
        this.groupId = this.$route.query.gid;
        this.isBlockEditGroupId = true;
        this.bitcoinWallet = group.wallets.bitcoin;
        this.total = group.cover.total;
        this.tinkoffWallet = group.wallets.tinkoff;
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
