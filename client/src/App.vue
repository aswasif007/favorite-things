<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-md-12 position-fixed app-title">
        Favorite Things
      </div>
    </div>
    <div class="row app-body">
      <div class="col">
        <div class="position-fixed left-panel">
          <left-panel :categories="categories" />
        </div>
      </div>
      <div class="col-sm-6 col-md-8 col-lg-9">
        <main-panel />
      </div>
    </div>
  </div>
</template>

<script>
import MainPanel from './main_panel/MainPanel.vue';
import LeftPanel from './left_panel/LeftPanel.vue';

import { getCategories } from './services';

export default {
  name: 'app',
  data () {
    return {
      categories: [],
    };
  },
  created () {
    this.fetchCategories();
  },
  components: {
    MainPanel,
    LeftPanel,
  },
  methods: {
    async fetchCategories () {
      const categoryResp = await getCategories();
      this.categories = categoryResp.data;
    },
  },
}
</script>

<style lang="scss" scoped>
@import "./_variables.scss";

.app-title {
  font-size: 40px;
  font-weight: 600;
  padding: 15px;
  z-index: 10;
  background: $White;
}

.app-body {
  padding-top: 100px;

  .left-panel {
    z-index: 10;
  }
}
</style>
