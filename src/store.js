const axios = require('axios');

module.exports = {
  state: {
    groups: [],
    group: {},
    api: 'vk-donatelo.herokuapp.com'
  },
  commits: {
    setGroups(state, data) {
      state.groups = data;
    },
    setGroup(state, data) {
      state.group = data;
    }
  },
  actions: {
    async loadGroups({state}, uid) {
      let resp = await axios.get(state.api + '/groups_list', {params: {uid}});
      state.commit('setGroups', resp.body);
    },
    async loadGroup({state}, {uid, gid}) {
      let resp = await axios.get(state.api + '/group_info', {params: {gid, uid}});
      state.commit('setGroup', resp.body);
    }
  }
}
