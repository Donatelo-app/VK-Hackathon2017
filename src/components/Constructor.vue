<template>
  <div id="constructor">
    <canvas id="playground"></canvas>
    <div class="container">
      <div class="row">
        <div class="col s3">
          <div @click="addNewTextNode" class="card-panel">
            Add text
          </div>
        </div>
        <div class="col s3">
          <div @click="addNewProgressBar" class="card-panel">
            Bar 1
          </div>
        </div>
        <div class="col s3">
          <div class="card-panel">
            Bar 2
          </div>
        </div>
        <div class="col s3">
          <div class="card-panel">
            Bar 3
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
  module.exports = {
    data() {
      return {
        scale: 1,
        views: [],
        gid: this.$route.query.gid,
        idNodes: 0
      }
    },
    methods: {
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
            angle: d.angle, border: d.border, color: d.fill,
            type: d.type, stand: d.stand, progress: d.progress,
            size: d.fontSize, font: d.fontNameOriginal, text: d.text
          });
          console.log(d);
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
      },
      addProgressBar(data) {
        let br = data.border || 0;
        let w = data.w  || 300;
        let h = data.h  || 30;
        let x = data.x || 150;
        let y = data.y || 150;
        let src_progress = data.progress;
        let src_stand = data.stand != null ? data.stand : 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTnU1rJkAAAADUlEQVQYV2P4//8/AwAI/AL+iF8G4AAAAABJRU5ErkJggg==';

        fabric.Image.fromURL('data:image/png;base64,' + src_stand.replace('data:image/png;base64,'), (stand) => {
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

          fabric.Image.fromURL('data:image/png;base64,' + src_progress.replace('data:image/png;base64,'), (progress) => {
            progress.scale(this.scale);
            progress.setWidth(w);
            progress.setHeight(h);

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
            });
            group.setOriginToCenter();
            group.angle = 180+ data.angle;
            group.id = this.idNodes++;
            group.selection = true;
            group.progress = src_progress;
            group.border = br;
            group.stand = src_stand;
            group.type = 'lineral';
            canvas.add(group);

          });
        });
      }
    },
    mounted() {
      window.canvas = new fabric.Canvas('playground');
      canvas.setWidth(window.innerWidth);

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
  .col {
    padding: 0 5px;
    border-radius: 10px;
  }
  .card-panel {
    height: 150px;
  }
  button {
    position: fixed;
    bottom: 25px;
    right: 25px;
  }
</style>
