const Vue = require('vue');
const VueRouter = require('vue-router');
const Vuex = require('vuex');

const store = require('./store')

const App = require('./components/App.vue');
const Constructor = require('./components/Constructor.vue');
const Groups = require('./components/Groups.vue');
const CreateGroup = require('./components/CreateGroup.vue');

Vue.use(VueRouter);
Vue.use(Vuex);

var router = new VueRouter({
	routes: [
		{path: '/', redirect: '/groups'},
		{path: '/groups', component: Groups},
		{path: '/edit', component: Constructor},
		{path: '/create', component: CreateGroup}
	]
});

new Vue({
  el: '#app',
	render: (h) => h(App),
	router,
	store: new Vuex.Store(store)
});
