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


fabric.Object.prototype.setOriginToCenter = function () {
    this._originalOriginX = this.originX;
    this._originalOriginY = this.originY;

    var center = this.getCenterPoint();

    this.set({
        originX: 'center',
        originY: 'center',
        left: center.x,
        top: center.y
    });
};

fabric.Object.prototype.setCenterToOrigin = function () {
    var originPoint = this.translateToOriginPoint(
    this.getCenterPoint(),
    this._originalOriginX,
    this._originalOriginY);

    this.set({
        originX: this._originalOriginX,
        originY: this._originalOriginY,
        left: originPoint.x,
        top: originPoint.y
    });
};

new Vue({
  el: '#app',
	render: (h) => h(App),
	router,
	store: new Vuex.Store(store)
});
