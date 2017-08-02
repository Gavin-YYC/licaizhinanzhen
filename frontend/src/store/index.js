import Vue         from 'vue';
import Vuex        from 'vuex';
import vueResource from 'vue-resource';

import state      from './state.js';
import actions    from './actions.js';
import mutations  from './mutations.js';

Vue.use( Vuex );
Vue.use( vueResource );

actions.use( Vue );

Vue.http.options.emulateJSON = true;
Vue.http.options.timeout = 10000;

Vue.http.interceptors.push((request, next)  => {
  next((response) => {
    if ( response.body.ret !== 0 ) {
      console.log( response.body.msg );
      return;
    }
  });
});

export default new Vuex.Store({
  state,
  actions,
  mutations
});
