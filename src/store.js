const axios = require('axios');

module.exports = {
  state: {
    groups: {
      'oxxxyof': 'img/bg.jpg',
      'oxxxyof1': 'img/bg.jpg',
      'oxxxyof2': 'img/bg.jpg',
      'oxxxyof3': 'img/bg.jpg',
      'oxxxyof4': 'img/bg.jpg',
      'oxxxyof5': 'img/bg.jpg',
      'oxxxyof6': 'img/bg.jpg',
      'oxxxyof7': 'img/bg.jpg',
    },
    fonts: {
      'BEBAS': 'Bebas Neue',
      'ROBOTO': 'Roboto Regular',
      'ARIAL': 'Arial'
    },
    bars: [
      {
        progress: 'img/bar.png',
        stand: 'img/bar.png',
        border: 5,
        stand_color: '#FF3300',
        progress_color: '#FFFFFF',
        w: 300,
        h: 31
      },
      {
        progress: 'img/bar2.png',
        stand: 'img/bar.png',
        w: 200,
        h: 50
      }
    ],
    group: {},
    gid: '51',
    api: 'vk-donatelo.herokuapp.com'
  },
  mutations: {
    setGroups(state, data) {
      state.groups = data;
    },
    setGroup(state, data) {
      state.group = data;
    },
    removeGroup(state, gid) {
      state.groups.$remove(gid);
    }
  },
  actions: {
    async loadGroups({commit, state}) {
      let resp = await axios.get(state.api + '/groups_list', {params: {uid: state.uid}});
      commit('setGroups', resp.body);
    },
    async loadGroup({commit, state}, gid) {
      let resp = await axios.get(state.api + '/group_info', {params: {gid, uid: state.uid}});
      commit('setGroup', resp.body);
    },
    async uploadGroupData({comit, state}, data) {
      data.uid = state.uid;
      let resp = await axios.post(state.api + '/update_group', data);
    },
    async removeGroup({commit, state}, gid) {
      let resp = await axios.post(state.api + '/remove_group', {gid, uid: state.uid});
      commit('removeGroup', gid);
    }
  }
}
