const Vue = require('vue');
const VueRouter = require('vue-router');
const Vuex = require('vuex');

const store = require('./store')

const App = require('./component/App.vue');
const Constructor = require('./component/Constructor.vue');

Vue.use(VueRouter);
Vue.use(Vuex);

var router = new VueRouter({
	routes: [
		{path: '/', redirect: '/edit'},
		{path: '/edit', component: Constructor},
	]
});

new Vue({
  el: '#app',
	render: (h) => h(App),
	router,
	store: new Vuex.Store(store)
});
