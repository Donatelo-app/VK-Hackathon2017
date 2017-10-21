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
    methods: {
      addTextNode() {
        var iText = new fabric.IText('Ваш текст', {
          left: 50,
          top: 50,
          fill: 'white',
          fontFamily: 'Bebas Neue',
          fontWeight: 'normal',
          fontSize: 60,
          padding: 7
        });
        iText.scale(this.scale);
        canvas.add(iText);
      },
      addProgressBar(id) {
        let data = this.$store.state.bars[0];

        fabric.Image.fromURL(data.progress, (stand) => {
          stand.selected = true;
          stand.setWidth(data.w+data.border*2);
          stand.setHeight(data.h+data.border*2);
          stand.left -= data.border;
          stand.top -= data.border;
          stand.scale(this.scale);
          var filter = new fabric.Image.filters.Tint({
            color: data.stand_color,
            opacity: 1
          });
          stand.filters.push(filter);
          stand.applyFilters(canvas.renderAll.bind(canvas));


          fabric.Image.fromURL(data.progress, (progress) => {
            progress.scale(this.scale);
            progress.setWidth(data.w/2);
            progress.setHeight(data.h);
            var filter = new fabric.Image.filters.Tint({
              color: data.progress_color,
              opacity: 1
            });
            progress.filters.push(filter);
            progress.applyFilters(canvas.renderAll.bind(canvas));

            var group = new fabric.Group([stand, progress], {
              left: 100,
              top: 25,
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
