<template>
  <div id="LeftPanel">
    <div class="header">
      <span class="title">Categories</span>
      <span @click="showAddCategory" class="action"><i class="fas fa-plus"></i></span>
    </div>
    <div class="body">
      <div class="category" v-for="category in categories" :key="category.guid">
        <div class="dot" :style="{color: category.color_code}">&bull;</div>
        <div class="title">{{category.title}}</div>
        <div @click="deleteCategory(category)" class="action"><i class="fas fa-trash"></i></div>
      </div>
      <div v-if="newCategory" class="category">
        <div class="dot" :style="{color: newCategory.color_code}">&bull;</div>
        <input type="text" placeholder="Add new category..."
          ref="titleInput"
          v-model="newCategory.title"
          @blur="hideAddCategory"
          @keypress.enter="createCategory"
        >
      </div>
    </div>
  </div>
</template>

<script>
import EventBus from '../eventBus';

import { getCategories } from '../services';

export default {
  name: 'LeftPanel',
  props: ['categories'],
  data () {
    return {
      newCategory: null,
    };
  },
  methods: {
    showAddCategory () {
      this.newCategory = {
        title: '',
        color_code: '#' + Math.random().toString(16).slice(2, 8),
      };
      setTimeout(() => this.$refs.titleInput.focus());
    },
    hideAddCategory () {
      this.newCategory = null;
    },
    createCategory () {
      EventBus.$emit('create-category', this.newCategory);
      this.hideAddCategory();
    },
    deleteCategory (category) {
      EventBus.$emit('delete-category', category);
    },
  }
}
</script>

<style lang="scss">
@import '../_variables.scss';

#LeftPanel {
  position: relative;

  .header {
    position: relative;
    font-size: 16px;
    margin-top: 2px;

    .title {
      font-weight: bold;
    }

    .action {
      position: absolute;
      right: 0;
      top: 0;

      i {
        opacity: 0.7;
        cursor: pointer;

        &:hover {
          opacity: 1;
          color: $DodgerBlue;
        }
      }
    }
  }

  .body {
    margin-top: 25px;
    width: 220px;

    .category {
      position: relative;
      line-height: 25px;
      margin: 5px 0;
      border-radius: 3px;

      .dot {
        position: absolute;
        font-size: $CategoryDotSize;
        line-height: 23px;
      }

      .title, input {
        font-size: 14px;
        font-weight: bold;
        margin-left: 10px;
        padding-left: 5px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        border: none;
      }

      .action {
        position: absolute;
        right: 0;
        top: 0;
        opacity: 0.7;
        font-size: 14px;
        display: none;

        &:hover {
          color: $DodgerBlue;
          opacity: 1;
          cursor: pointer;
        }
      }

      &:hover {
        .action {
          display: block;
        }

        .title {
          margin-right: 15px;
        }
      }
    }
  }
}
</style>
