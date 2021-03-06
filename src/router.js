import Vue from 'vue'
import Router from 'vue-router'

import DashboardView from './views/Dashboard.vue'
import ApplicationView from './views/Application.vue'
import FileBrowser from './views/FileBrowser'
import MonitoringView from './views/Monitoring.vue'
import SettingsView from './views/Settings.vue'
import UsersView from './views/Users.vue'
import AddServerView from './views/AddServer.vue'
import ClientKeysView from './views/ClientKeys.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: DashboardView,
    },
    {
      path: '/applications',
      name: 'Applications',
      component: ApplicationView,
    },
    {
      path: '/clientkeys',
      name: 'Client Keys',
      component: ClientKeysView,
    },
    {
      path: '/filebrowser',
      name: 'File Browser',
      component: FileBrowser,
    },
    {
      path: '/monitoring',
      name: 'Monitoring',
      component: MonitoringView,
    },
    {
      path: '/settings',
      name: 'Settings',
      component: SettingsView,
    },
    {
      path: '/users',
      name: 'Users',
      component: UsersView,
    },
    {
      path: '/addserver',
      name: 'Add Server',
      component: AddServerView,
    },
  ]
})
