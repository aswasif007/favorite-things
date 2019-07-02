<template>
  <div id="MainPanel">
    <div class="row">
      <div class="col-8">
        <div class="position-fixed search-bar">
          <input type="text" v-model="query" @keyup="searchItems">
          <span><i class="fa fa-search"></i></span>
        </div>
      </div>
      <div class="col-4">
        <div class="float-right">
          <div class="position-fixed action-bar">
            <span><i class="fas fa-grip-horizontal"></i></span>
            <span><i class="fas fa-bars"></i></span>
            <span @click="openModal({})"><i class="fas fa-plus"></i></span>
          </div>
        </div>
      </div>
    </div>
    <div class="item-container">
      <grid-view
        :items="items"
        :showItem="openModal"
      />
    </div>
    <item-modal v-if="!!modalItem"
      :categories="categories"
      :item="modalItem"
      :close="closeModal"
    />
  </div>
</template>

<script>
import * as _ from 'lodash';

import EventBus from '../eventBus';

import ItemModal from './ItemModal.vue';
import GridView from './grid_view/GridView.vue';

export default {
  name: "MainPanel",
  props: ['categories', 'items'],
  data() {
    return {
      modalItem: null,
      query: '',
    };
  },
  components: {
    GridView,
    ItemModal,
  },
  methods: {
    openModal(item) {
      this.modalItem = item;
    },
    closeModal() {
      this.modalItem = null;
    },
    searchItems: _.debounce(function() {
      EventBus.$emit('refresh-items', {q: this.query});
    }, 500),
  },
}
</script>

<style lang="scss">
@import "../_variables.scss";

#MainPanel {
  .search-bar {
    margin: -10px -50%;
    padding: 10px 50%;
    background: $White;
    width: 150%;
    box-shadow: 1px 1px 2px $MediumGray;
    z-index: 9;

    input {
      margin-left: -10px;
      padding-left: 5px;
      padding-right: 28px;
      border: 1px solid $MediumGray;
      border-radius: 3px;
    }

    span {
      margin-left: -27px;
      opacity: 0.4;
      
      i {
        font-size: 14px;
      };
    }
  }
  
  .action-bar {
    margin-left: -70px;
    z-index: 10;
    padding-top: 3px;
  
    span {
      margin-left: 10px;
      cursor: pointer;
      opacity: 0.7;
  
      &:hover {
        opacity: 1;
        color: $DodgerBlue;
      }
    }
  }
  
  .item-container {
    padding-top: 20px;
    margin-top: 30px;
  }
}
</style>
