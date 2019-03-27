import Vue from 'vue'
import App from './App.vue'
import router from './router'

import db from './datastore'
import store from './store'
import './registerServiceWorker'

Vue.config.productionTip = false
Vue.prototype.$db = db

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
