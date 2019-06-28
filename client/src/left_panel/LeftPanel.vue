<template>
  <div id="LeftPanel">
    <div class="header">
      <span class="title">Categories</span>
      <span class="action"><i class="fas fa-plus"></i></span>
    </div>
    <div class="body">
      <div class="category" v-for="category in categories" :key="category.guid">
        <div class="dot" :style="{color: category.color_code}">&bull;</div>
        <div class="title">{{category.title}}</div>
      </div>
    </div>
  </div>  
</template>

<script>
import { getCategories } from '../services';

export default {
  name: 'LeftPanel',
  props: ['categories'],
}
</script>

<style lang="scss">
@import '../_variables.scss';

#LeftPanel {
  position: relative;

  .header {
    position: relative;
    font-size: 16px;
    width: 140px;

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
        }
      }
    }
  }

  .body {
    margin-top: 25px;

    .category {
      position: relative;
      line-height: 22px;
      margin: 5px -5px;
      padding: 0 5px;
      width: 140px;
      border-radius: 3px;
      transition: background-color 0.4s ease;

      .dot {
        position: absolute;
        font-size: $CategoryDotSize;
      }

      .title {
        font-size: 14px;
        font-weight: bold;
        margin-left: 15px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      &:hover {
        cursor: pointer;
        background-color: $PowderBlue;
      }
    }
  }
}
</style>
