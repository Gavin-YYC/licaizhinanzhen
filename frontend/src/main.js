import Vue from 'vue';
import app from './app.vue';

import store from './store/index.js';

Vue.use(store);

new Vue({
  el: '#app',
  store,
  render: h => h( app )
});
