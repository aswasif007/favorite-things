<template>
  <div id="MainPanel">
    <div class="row task-bar">
      <div class="col-8">
        <div class="position-fixed search-bar">
          Searchbar
        </div>
      </div>
      <div class="col-4">
        <div class="float-right">
          <div class="position-fixed action-bar">
            Actions
          </div>
        </div>
      </div>
    </div>
    <div class="item-container">
      <grid-view :items="items" />
    </div>
  </div>
</template>

<script>
import GridView from './grid_view/GridView.vue';
import { getItems } from '../services';

export default {
  name: "MainPanel",
  data () {
    return {
      items: [],
    };
  },
  created () {
    this.fetchItems();
  },
  components: {
    GridView
  },
  methods: {
    async fetchItems () {
      const itemResp = await getItems();
      this.items = itemResp.data;
    },
  }
}
</script>

<style lang="scss">
@import "../_variables.scss";

.search-bar {
  margin: -10px -50%;
  padding: 10px 50%;
  background: $White;
  width: 150%;
  box-shadow: 1px 1px 2px $MediumGray;
  z-index: 9;
}

.action-bar {
  margin-left: -50px;
  z-index: 10;
}

.item-container {
  padding-top: 20px;
  margin-top: 30px;
}
</style>
