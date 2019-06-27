<template>
  <div id="GridView" class="row">
    <div v-for="index in 10" :key="index" class="col-sm-12 col-md-6 col-lg-4 cards">
      <card />
    </div>
  </div>
</template>

<script>
import Card from './Card.vue';

export default {
  name: 'GridView',
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
