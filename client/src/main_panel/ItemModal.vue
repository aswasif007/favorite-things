<template>
  <div @click="close" id="ItemModal">
    <div class="modal-view" @click="event => event.stopPropagation()">
      <div class="header">
        <input ref="title" type="text" placeholder="Title goes here..."
          v-if="isEditable" 
          v-model="displayItem.title"
        >
        <div v-else class="title">{{displayItem.title}}</div>
      </div>
      <hr>
      <div class="body">
        <textarea placeholder="Description goes here"
          v-if="isEditable" 
          v-model="displayItem.description"
        />
        <div v-else class="description">{{displayItem.description}}</div>
      </div>
      <hr>
      <div class="footer">
        <span class="category-dot" :style="{color: colorCode}">
          <i :class="`${displayItem.category ? 'fas' : 'far'} fa-circle`"></i>
        </span>
        <select v-if="isEditable" v-model="displayItem.category">
          <option :value="undefined" disabled selected hidden>Choose category...</option>
          <option v-for="category in categories" :key="category.guid" :value="category.guid">{{category.title}}</option>
        </select>
        <div v-else class="category">{{displayItem.category_obj.title}}</div>

        <div class="actions">
          <span v-if="isEditable">
            <span @click="discardEdit" class="icon"><i class="fas fa-times"></i></span>
            <span @click="handleSave" class="icon"><i class="fas fa-check"></i></span>
          </span>
          <span v-else>
            <span class="timestamp">Last updated: {{displayItem.modified_at | formatTimestamp}}</span>
            <span @click="setEditable" class="icon"><i class="fas fa-edit"></i></span>
            <span @click="handleDelete" class="icon"><i class="fas fa-trash"></i></span>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import moment from 'moment';

import EventBus from '../eventBus';

export default {
  name: 'ItemModal',
  props: ['categories', 'item', 'close'],
  data() {
    return {
      displayItem: _.clone(this.item),
      isEditable: _.isEmpty(this.item),
    };
  },
  mounted() {
    if (this.isEditable) {
      this.$refs.title.focus();
    }
  },
  filters: {
    formatTimestamp(timestamp) {
      return moment(timestamp).fromNow();
    },
  },
  computed: {
    colorCode() {
      const category = _.find(this.categories, {'guid': this.displayItem.category});
      return _.get(category, 'color_code', '#000');
    },
  },
  methods: {
    setEditable() {
      this.isEditable = true;
      setTimeout(() => this.$refs.title.focus());
    },
    handleDelete() {
      // TODO
    },
    discardEdit() {
      this.displayItem = this.item;
      this.isEditable = _.isEmpty(this.item);
    },
    handleSave() {
      if (this.displayItem.guid) {
        EventBus.$emit('update-item', _.pick(this.displayItem, ['guid', 'title', 'category', 'description']));
      } else {
        EventBus.$emit('create-item', this.displayItem);
      }
      this.close();
    },
  }
}
</script>

<style lang="scss">
@import '../_variables';

#ItemModal {
  background: rgba($color: $White, $alpha: 0.8);
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  z-index: 100;
  position: fixed;

  .modal-view {
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    margin: 0 auto;
    border: 1px solid $MediumGray;
    border-radius: 3px;
    width: 700px;
    height: 450px;
    background: $White;
    padding: 15px;
    box-shadow: 0 0 5px $MediumGray;

    .header {
      margin: 10px 0;

      .title, input {
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        overflow-y: hidden;
        border: none;
        padding: 0 5px;
        height: 30px;
      }
    }

    hr {
      margin: 5px 0;
    }

    .body {
      width: 100%;
      height: calc(100% - 110px);

      .description, textarea {
        resize: none;
        width: 100%;
        height: 100%;
        border: none;
        padding: 5px;
        text-align: justify;
      }
    }

    .footer {
      margin-top: 15px;

      .category, select {
        display: inline-block;
        background: none;
        border: none;
        padding: 5px 0;
      }

      .category {
        padding: 3px 0 0 4px;
      }

      .actions {
        display: inline-block;
        position: absolute;
        right: 15px;
        
        .icon {
          margin-left: 10px;
          opacity: 0.7;
          cursor: pointer;

          &:hover {
            opacity: 1;
            color: $DodgerBlue;
          }
        }

        .timestamp {
          font-size: 12px;
          line-height: 30px;
          color: $Gray;
        }
      }
    }
  }
}
</style>
