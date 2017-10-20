<template>
  <div id="constructor">
    <h1>DonateLo</h1>
    <div style="height: 500px; width: 500px;float:left;position: relative;border: 1px solid black;padding:5px">
      <vue-drr :w='180' :h='180' :bounds='{parent:true}' :rotatable='true'>
        <textarea style="height: 100%">ПАЦАНЫ, КИНЬТЕ БАБОК НА ПИТЕР, В ЭТОТ РАЗ Я ЕГО ТОЧНО ВЫЕБУ</textarea>
      </vue-drr>
    </div>
  </div>
</template>

<script>
  const VueDRR = require('./DRR.vue');

  module.exports = {
    name: 'app',
    components: {
      'vue-drr': VueDRR
    },
    methods: {
      showchange(data) {
        console.log(JSON.stringify(data))
      }
    }
  }
</script>
