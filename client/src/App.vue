<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-md-12 position-fixed app-title">
        Favorite Things
      </div>
    </div>
    <div class="row app-body">
      <div class="col">
        <div class="position-fixed">
          CATEGORIES
        </div>
      </div>
      <div class="col-sm-4 col-md-6 col-lg-8">
        <main-panel />
      </div>
      <div class="col">
        <div class="position-fixed app-logs">
          LOGS
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MainPanel from './main_panel/MainPanel.vue';

export default {
  name: 'app',

  components: {
    MainPanel,
  }
}
</script>

<style lang="scss" scoped>
@import "./_variables.scss";

.app-title {
  font-size: 40px;
  font-weight: 600;
  padding: 15px 0;
  z-index: 10;
  background: $White;
}

.app-logs {
  margin: -20px -15px;
  padding: 20px 15px;
  background: $White;
  width: 100%;
  z-index: 10;
}

.app-body {
  padding-top: 100px;
  height: 1500px;
}
</style>
