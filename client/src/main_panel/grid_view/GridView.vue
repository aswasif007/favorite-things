<template>
  <div id="GridView" class="row">
    <div v-for="item in items" :key="item.guid" class="col-sm-12 col-md-6 col-lg-4 col-xl-3 cards">
      <card
        @click.native="showItem(item)"
        :item="item"
      />
    </div>
  </div>
</template>

<script>
import Card from './Card.vue';

export default {
  name: 'GridView',
  props: ['items', 'showItem'],
  components: {
    Card,
  }
}
</script>

<style lang="scss">
.cards {
  padding: 5px;
}
</style>
