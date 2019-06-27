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
    <div class="row item-container">
      Items
    </div>
  </div>
</template>

<script>
export default {
  name: "MainPanel",
}
</script>

<style lang="scss">
@import "../_variables.scss";

.search-bar {
  margin: -10px -15px;
  padding: 10px 15px;
  background: $White;
  width: 100%;
  box-shadow: 2px 4px 4px $LightGray;
}

.action-bar {
  margin-left: -50px
}

.item-container {
  padding-top: 20px;
  margin-top: 30px;
}
</style>
