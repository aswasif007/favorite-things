import axios from 'axios';

const API = 'http://localhost:8000/api/v0/';

function getItems() {
  const url = API + 'items/';
  return axios.get(url);
}

function createItem(item) {
  const url = API + 'items/';
  return axios.post(url, item);
}

function updateItem(item) {
  const url = API + 'items/' + item.guid;
  return axios.put(url, item);
}

function deleteItem(itemGuid) {
  const url = API + 'items/' + itemGuid;
  return axios.delete(url);
}

function getCategories() {
  const url = API + 'categories/';
  return axios.get(url);
}

function createCategory(category) {
  const url = API + 'categories/';
  return axios.post(url, category);
}

function deleteCategory(categoryGuid) {
  const url = API + 'categories/' + categoryGuid;
  return axios.delete(url);
}

export {
  getItems,
  createItem,
  updateItem,
  deleteItem,
  getCategories,
  createCategory,
  deleteCategory,
};
