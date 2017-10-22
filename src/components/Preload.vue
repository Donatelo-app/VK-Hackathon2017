<template>
  <div class="preloader-wrapper big active">
    <div class="spinner-layer spinner-blue">
      <div class="circle-clipper left">
        <div class="circle"></div>
      </div><div class="gap-patch">
        <div class="circle"></div>
      </div><div class="circle-clipper right">
        <div class="circle"></div>
      </div>
    </div>
  </div>
</template>

<style media="screen">
  .preloader-wrapper {
    top: 50%;
    left: 50%;
    z-index: 100000000;
    margin: -32px;
    position: fixed;
  }
</style>
