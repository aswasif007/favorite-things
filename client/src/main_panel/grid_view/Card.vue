<template>
  <div id="Card" class="card">
    <div class="category-dot" :style="{color: item.category_obj.color_code}">&bull;</div>
    <div class="title">{{item.title}}</div>
    <div class="rank">#{{item.rank}}</div>
    <div class="actions">
      <i class="fas fa-edit"></i>
      <i class="fas fa-trash"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: ['item'],
}
</script>

<style lang="scss">
@import "../../_variables.scss";

.card {
  height: 100px;
  width: 100%;
  background: #eee;
  padding: 5px;
  position: relative;
  transition: box-shadow 0.2s ease;

  .category-dot {
    position: absolute;
    font-size: 28px;
    line-height: 22px;  
  }

  .title {
    margin-left: 15px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .rank {
    position: absolute;
    bottom: 5px;
    left: 5px;
    font-size: 16px;
    font-weight: bold;
    font-family: monospace;
  }

  .actions {
    position: absolute;
    bottom: 5px;
    right: 5px;
    display: none;

    i {
      margin-right: 5px;
      font-size: 14px;
      opacity: 0.6;

      &:hover {
        opacity: 1;
      }
    }
  }

  &:hover {
    cursor: pointer;
    box-shadow: 0 0 6px $DodgerBlue;
    .actions {
      display: block;
    }
  }
}
</style>
