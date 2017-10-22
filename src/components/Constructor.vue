<template>
  <div id="constructor">
    <nav>
      <div class="nav-wrapper vk-color">
        <p class="flow-text">Редактор обложки:</p>
      </div>
    </nav>
    <canvas id="playground"></canvas>
    <div v-show="openTab === 'menu'" id="menu" class="container">
      <div class="row">
        <div class="col s3">
          <div @click="addNewTextNode" class="card-panel hoverable">
            <i class="material-icons">text_format</i>
            <p>Добавить текст</p>
          </div>
        </div>
        <div class="col s3">
          <div @click="addNewProgressBar" class="card-panel hoverable">
            <i class="material-icons">format_align_left</i>
            <p>Cтандарный бар</p>
          </div>
        </div>
        <div class="col s3">
          <div class="card-panel hoverable">
            <input type="file" class="select-image" id="new-progressbar" @change="addCustomProgressBar">
            <i class="material-icons">extension</i>
            <p>Загрузить бар</p>
          </div>
        </div>
        <div class="col s3">
          <router-link :to="{path: 'info_group', query: {gid}}">
            <div class="card-panel hoverable">
              <i class="material-icons">settings</i>
              <p>Настроики</p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    <div v-show="openTab === 'text'" id="text" class="container">
      <div class="row">
        <div class="col s2">
          <div @click="backToMenu" class="card-panel hoverable">
            <i class="material-icons">keyboard_arrow_left</i>
            <p>Назад</p>
          </div>
        </div>
        <div class="col s7">
          <div class="card-panel not-gradient" style="cursor: default">
            <div class="col s7">
              <div class="input-field col s12">
                <select v-model="font">
                  <option value="BEBAS" selected>BEBAS</option>
                </select>
                <label>Шрифт</label>
              </div>
              <div class="input-field col s12">
                <input id="fontsize" v-model="fontsize"  type="number" required class="validate">
                <label class="active" for="fontsize">Размер:</label>
              </div>
            </div>
            <div class="col s5">
              <chrome-picker v-model="colors" @input="updateColor"/>
            </div>
          </div>
        </div>
        <div class="col s3">
          <div @click="removeObject" class="card-panel hoverable">
            <i class="material-icons">delete</i>
            <p>Удалить</p>
          </div>
        </div>
      </div>
    </div>
    <div v-show="openTab === 'progressbar'" id="progressbar" class="container">
      <div class="row">
        <div class="col s2">
          <div @click="backToMenu" class="card-panel hoverable">
            <i class="material-icons">keyboard_arrow_left</i>
            <p>Назад</p>
          </div>
        </div>
        <div class="col s7">
          <div class="card-panel hoverable">
            <input type="file" class="select-image" editCurrentProgressBar>
            <i class="material-icons">mode_edit</i>
            <p>Заменить исходную картинку</p>
          </div>
        </div>
        <div class="col s3">
          <div @click="removeObject" class="card-panel hoverable">
            <i class="material-icons">delete</i>
            <p>Удалить</p>
          </div>
        </div>
      </div>
    </div>

    <button id="upload_data" @click="uploadData" class="btn-floating btn-large waves-effect waves-light vk-color">
      <i class="material-icons">check</i>
    </button>
  </div>
</template>

<script>
  const Chrome = require('vue-color/dist/vue-color.min.js').Chrome;

  module.exports = {
    components: {
       'chrome-picker': Chrome
    },
    data() {
      return {
        colors: '',
        fontsize: 36,
        scale: 1,
        views: [],
        font: 'BEBAS',
        gid: this.$route.query.gid,
        idNodes: 0,
        openTab: 'menu'
      }
    },
    watch: {
      colors() {
        this.selectObject.fill = this.colors.hex;
      },
      fontsize() {
        this.selectObject.fontSize = this.fontsize;
      },
      font() {
        this.selectObject.fontFamily = this.font;
      }
    },
    methods: {
      addCustomProgressBar(e) {
        console.log(e)

        var files = e.target.files || e.dataTransfer.files;
        if(!files.length) return;

        console.log('dfdsf')
        console.log(files)

        var reader = new FileReader();
        reader.onload = (e) => {
          console.log(e.target)
          this.addProgressBar({
            progress: e.target.result,
            stand: null,
            x: 300,
            y: 300,
            border: 0,
            angle: 0,
            w: 300,
            h: 300
          });
        };
        reader.readAsDataURL(files[0]);
      },
      editCurrentProgressBar(e) {
        var files = e.target.files || e.dataTransfer.files;
        if(!files.length) return;

        var reader = new FileReader();
        reader.onload = (e) => {
          this.currentObject.item(1).setSrc(e.target.result);
        };
        reader.readAsDataURL(files[0]);
      },
      removeObject() {
        canvas.remove(this.selectObject);
        this.openTab = 'menu';
      },
      backToMenu() {
        this.openTab = 'menu';
      },
      addNewTextNode() {
        this.addTextNode({
          y: 150,
          text: 'Ваш текст',
          x: 150,
          color: '#000000',
          font: 'BEBAS',
          size: 40
        });
      },
      addNewProgressBar() {
        this.addProgressBar(this.$store.state.bars[0]);
      },
      uploadData() {
        let data = {gid: this.gid, info: this.$store.state.group};
        data.info.cover.views = [];

        let c = 0;
        for(let key in canvas._objects) {
          if(!c) {
            c++; continue;
          }

          let d = canvas._objects[key];
          data.info.cover.views.push({
            x: Math.floor(d.left/this.scale), y: Math.floor(d.top/this.scale),
            w: Math.floor(d.currentWidth/this.scale), h: Math.floor(d.currentHeight/this.scale),
            angle: d.angle-180, border: d.border, color: d.fill,
            type: d.type, stand: d.stand, progress: d.progress,
            size: +d.fontSize, font: d.fontNameOriginal, text: d.text
          });
        }

        this.$store.dispatch('uploadData', data);
      },

      addTextNode(data) {
        var iText = new fabric.IText(data.text, {
          left: data.x*this.scale,
          top: data.y*this.scale,
          fill: data.color,
          fontFamily: this.$store.state.fonts[data.font],
          fontSize: data.size,
          padding: 7
        });
        iText.id = this.idNodes++;
        iText.fontNameOriginal = data.font;
        iText.type = 'text';
        iText.selectable = true;

        iText.scale(this.scale);
        canvas.add(iText);

        iText.on('mousedown', () => {
          this.selectObject = iText;
          this.font = iText.fontFamily;
          this.fontsize = iText.fontSize;
          this.colors.hex = iText.fill;
          this.openTab = 'text';
        });
      },
      addProgressBar(data) {
        let br = data.border || 0;
        let w = data.w  || 300;
        let h = data.h  || 30;
        let x = data.x || 150;
        let y = data.y || 150;
        let src_progress = data.progress;
        let src_stand = data.stand != null ? data.stand : 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTnU1rJkAAAADUlEQVQYV2P4//8/AwAI/AL+iF8G4AAAAABJRU5ErkJggg==';

        fabric.Image.fromURL('data:image/png;base64,' + src_stand.replace('data:image/png;base64,', ''), (stand) => {
          stand.selected = true;
          stand.setWidth(w+br*2);
          stand.setHeight(h+br*2);
          stand.left = -br;
          stand.top = -br;
          stand.scale(this.scale);

          if(data.stand_color) {
            var filter = new fabric.Image.filters.Tint({
              color: data.stand_color,
              opacity: 1
            });
            stand.filters.push(filter);
            stand.applyFilters(canvas.renderAll.bind(canvas));
          }

          fabric.Image.fromURL('data:image/png;base64,' + src_progress.replace('data:image/png;base64,', ''), (progress) => {
            progress.scale(this.scale);
            progress.setWidth(w);
            progress.setHeight(h);
            progress.selectable = true;

            if(data.progress_color) {
              var filter = new fabric.Image.filters.Tint({
                color: data.progress_color,
                opacity: 1
              });
              progress.filters.push(filter);
              progress.applyFilters(canvas.renderAll.bind(canvas));
            }

            var group = new fabric.Group([stand, progress], {
              left: x*this.scale-w*this.scale/2,
              top: y*this.scale-h*this.scale/2,
              selectable: true
            });
            group.setOriginToCenter();
            group.angle = data.angle+180;
            group.id = this.idNodes++;
            group.selectable = true;
            group.progress = src_progress;
            group.border = br;
            group.stand = data.stand;
            group.type = 'lineral';
            canvas.selection = false;
            canvas.add(group);

            group.on('mousedown', () => {
              this.selectObject = group;
              this.openTab = 'progressbar';
            })
          })
        })
      }
    },
    mounted() {
      window.canvas = new fabric.Canvas('playground');
      canvas.setWidth(window.innerWidth);

      $('select').material_select();
      $('.vc-chrome-fields-wrap').remove();

      this.$store.dispatch('loadGroup', {gid: this.$route.query.gid, cb: (data) => {
        fabric.Image.fromURL('data:image/png;base64,' + data.cover.background, (img) => {
          img.set('selectable', false);
          this.scale = window.innerWidth/img.getWidth();
          img.scale(this.scale);
          canvas.setHeight(img.getHeight());
          canvas.add(img);

          data.cover.views.forEach((view) => {
            if(!view) return;
            if(view.type === 'lineral') this.addProgressBar(view);
          });
          setTimeout(()=> {
            data.cover.views.forEach((view) => {
              if(!view) return;
              if(view.type === 'text') this.addTextNode(view);
            });
          }, 1000);
        });
      }})
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 10px;
  }
  .col {
    padding: 0 5px;
    border-radius: 10px;
  }
  .vc-chrome {
    width: 100%;
    margin-top: 13px;
    box-shadow: none;
  }
  .select-image {
    cursor: pointer;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
  }
  .not-gradient {
    height: 200px;
  }
  .vc-chrome-fields-wrap {
      display: none;
  }
  .card-panel {
    position: relative;
  }
  .card-panel:not(.not-gradient) {
    border-radius: 7px;
    cursor: pointer;
    height: 150px;
    text-align: center;
    background: -webkit-linear-gradient(#5e81a8, #b660bb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .card-panel i {
    background: -webkit-linear-gradient(#5e81a8, #b660bb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3em;
  }
  button {
    position: fixed;
    bottom: 25px;
    right: 25px;
  }
</style>
