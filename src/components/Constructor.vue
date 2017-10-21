<template>
  <div id="constructor">
    <canvas id="playground"></canvas>
    <div class="container">
      <div class="row">
        <div class="col s3">
          <div @click="addTextNode" class="card-panel">
            Add text
          </div>
        </div>
        <div class="col s3">
          <div @click="addProgressBar" class="card-panel">
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
  </div>
</template>

<script>
  module.exports = {
    data() {
      return {
        scale: 1
      }
    },
    computed: {
      data() {
        return this.$store.state.group;
      }
    },
    methods: {
      addTextNode(e, data = {}) {
        var iText = new fabric.IText(data.text || 'Введите текст', {
          left: data.x != null ? date.x : 50,
          top: data.y != null ? date.y : 50,
          fill: data.color || 'white',
          fontFamily: this.$store.state.fonts[data.font] || 'Bebas Neue',
          fontSize: data.size || 60,
          padding: 7
        });
        iText.scale(this.scale);
        canvas.add(iText);
      },
      addProgressBar(e, data = {}) {
        let br = data.border != null ? data.border : 0;
        let w = data.w || 300;
        let h = data.h || 40;
        let x = data.x != null ? data.x+w/2 : 50;
        let y = data.y != null ? data.y+h/2 : 50;
        let stand_color = data.stand_color || '#CCCCCC';
        let progress_color = data.progress_color || '#FFFFFF';

        fabric.Image.fromURL(data.progress || 'img/bar.png', (stand) => {
          stand.selected = true;
          stand.setWidth(w+br*2);
          stand.setHeight(h+br*2);
          stand.left -= -br;
          stand.top -= -br;
          stand.scale(this.scale);
          var filter = new fabric.Image.filters.Tint({
            color: stand_color,
            opacity: 1
          });
          stand.filters.push(filter);
          stand.applyFilters(canvas.renderAll.bind(canvas));


          fabric.Image.fromURL(data.progress || 'img/bar.png', (progress) => {
            progress.scale(this.scale);
            progress.setWidth(w/2);
            progress.setHeight(h);
            var filter = new fabric.Image.filters.Tint({
              color: progress_color,
              opacity: 1
            });
            progress.filters.push(filter);
            progress.applyFilters(canvas.renderAll.bind(canvas));

            var group = new fabric.Group([stand, progress], {
              left: x,
              top: y,
            });
            canvas.add(group);
          });
        });
      }
    },
    mounted() {
      window.canvas = new fabric.Canvas('playground');
      canvas.setWidth(window.innerWidth);
      canvas.setHeight(400);

      fabric.Image.fromURL('img/bg.jpg', (img) => {
        img.set('selectable', false);
        this.scale = window.innerWidth/img.getWidth();
        img.scale(this.scale);
        canvas.add(img);
      });
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
</style>
