import axios from 'axios';

const API = 'http://localhost:8000/api/v0/';

function getItems() {
  const url = API + 'items/';
  return axios.get(url);
}

function getCategories() {
  const url = API + 'categories/';
  return axios.get(url);
}

function createCategory(category) {
  const url = API + 'categories/';
  return axios.post(url, category);
}

export {
  getItems,
  getCategories,
  createCategory,
};
