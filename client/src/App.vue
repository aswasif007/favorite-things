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
          <left-panel
            :categories="categories"
          />
        </div>
      </div>
      <div class="col-sm-6 col-md-8 col-lg-9">
        <main-panel
          :items="items"
          :categories="categories"
        />
      </div>
    </div>
  </div>
</template>

<script>
import * as _ from 'lodash';
import EventBus from './eventBus';

import MainPanel from './main_panel/MainPanel.vue';
import LeftPanel from './left_panel/LeftPanel.vue';

import { getItems, createItem, updateItem, deleteItem, getCategories, createCategory, deleteCategory } from './services';

export default {
  name: 'app',
  data () {
    return {
      categories: [],
      items: [],
    };
  },
  created () {
    this.fetchCategories();
    this.fetchItems();

    EventBus.$on('refresh-items', this.fetchItems);
    EventBus.$on('create-item', this.createItem);
    EventBus.$on('update-item', this.updateItem);
    EventBus.$on('delete-item', this.deleteItem);

    EventBus.$on('refresh-categories', this.createCategory);
    EventBus.$on('create-category', this.createCategory);
    EventBus.$on('delete-category', this.deleteCategory);
  },
  components: {
    MainPanel,
    LeftPanel,
  },
  methods: {
    async fetchItems(params) {
      const itemResp = await getItems(params || {});
      this.items = itemResp.data;
    },
    async createItem(item) {
      if (!item.title.trim()) { item.title = 'New Item'; }

      const itemResp = await createItem(item);

      if (itemResp.status === 201) {
        this.items.unshift(itemResp.data);
      }
    },
    async updateItem(item) {
      if (!item.title.trim()) { item = _.omit('title'); }

      const itemResp = await updateItem(item);

      if (itemResp.status === 200) {
        this.items = _.filter(this.items, _item => _item.guid !== item.guid);
        this.items.unshift(itemResp.data);
      }
    },
    async deleteItem(item) {
      const itemResp = await deleteItem(item.guid);

      if (itemResp.status === 204) {
        this.items = _.without(this.items, item);
      }
    },
    async fetchCategories() {
      const categoryResp = await getCategories();
      this.categories = categoryResp.data;
    },
    async createCategory(category) {
      if (!category.title.trim()) { category.title = 'New Category'; }

      const categoryResp = await createCategory(category);

      if (categoryResp.status === 201) {
        this.categories.push(categoryResp.data);
      }
    },
    async deleteCategory(category) {
      const categoryResp = await deleteCategory(category.guid);

      if (categoryResp.status === 204) {
        this.categories = _.without(this.categories, category);
        EventBus.$emit('refresh-items');
      }
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
