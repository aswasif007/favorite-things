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
        <div class="action"><i class="fas fa-pen"></i></div>
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

      .title {
        font-size: 14px;
        font-weight: bold;
        margin-left: 15px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
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
