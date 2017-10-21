const axios = require('axios');

module.exports = {
  state: {
    groups: {},
    fonts: {
      'BEBAS': 'Bebas Neue',
      'ROBOTO': 'Roboto Regular',
      'ARIAL': 'Arial'
    },
    bars: [
      {
        progress: 'iVBORw0KGgoAAAANSUhEUgAAAZ8AAABBCAYAAAAOoal/AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTnU1rJkAAACkElEQVR4Xu3cQW7iQBAFUE6TRW7HNXKMbHNIxuWkrTYuwIBdEsN70pegpCRe8VVth8PpdNojn0O+RETkpXMckn3GP510+EDiAvsL/hkCwOv7HtJ/vsdykfXAXUmHK9O2m7gwAN5DLBfx2f/UVpQOb6SVju0G4L3F8vHQJpQOryT+iNIBoGmb0F0llA6T2HYAuCb6YXUBpcOz2HYAWGP1FpQOuygeAO51cwtKh39RPAA86moBpcMhigeAZ8URXNYxF8snfgAAnnFx+1kMhth6ANhKWkCzN0MUDwBbWxy/zd4McdwGwNYW209fPLYeAPYSX8WTlo+tB4A9TV9G2pcPAOxpuvfTiifaCAD2NN37aeXjyA2ACuP208oHACpM5fMxvgWA/U3l434PAFXGR67d7wGg2lH5AFDtS/kAUE35AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUG4sn+PvawAocYzy+fh9DQC7+x5yiPKJAECFuNUzlY/7PgBUmJWP+z4AVIi+mconAgB7Gu/3RPrycfQGwJ7GI7dIXz6O3gDYy8+QzyGL8onESgQAW5u2nkhfPJFopWgnANjKbOuJ9MXT4vgNgK0siicye9PF8RsAWxgfrT7PYvAXx28APGt6tPo86fAvCgiAR6XHbS3psIsCAuBeV4snkg7PooAAWCO6Ih6pvlo8kXSYJH5R/EIlBEDm5rbTJx1eiS0IgHPxYMHq4omkwxuxBQEQonTSR6lvJR2uTCsh/xME8D7afZ2HSqclHT6QuIi4GGUE8H9pZdNy1/HapaTDDdKXkYiIvG42KZt5Tod/OGkUGYvStAgAAAAASUVORK5CYII=',
        stand: 'iVBORw0KGgoAAAANSUhEUgAAAZ8AAABBCAYAAAAOoal/AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTnU1rJkAAACkElEQVR4Xu3cQW7iQBAFUE6TRW7HNXKMbHNIxuWkrTYuwIBdEsN70pegpCRe8VVth8PpdNojn0O+RETkpXMckn3GP510+EDiAvsL/hkCwOv7HtJ/vsdykfXAXUmHK9O2m7gwAN5DLBfx2f/UVpQOb6SVju0G4L3F8vHQJpQOryT+iNIBoGmb0F0llA6T2HYAuCb6YXUBpcOz2HYAWGP1FpQOuygeAO51cwtKh39RPAA86moBpcMhigeAZ8URXNYxF8snfgAAnnFx+1kMhth6ANhKWkCzN0MUDwBbWxy/zd4McdwGwNYW209fPLYeAPYSX8WTlo+tB4A9TV9G2pcPAOxpuvfTiifaCAD2NN37aeXjyA2ACuP208oHACpM5fMxvgWA/U3l434PAFXGR67d7wGg2lH5AFDtS/kAUE35AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUE75AFBO+QBQTvkAUG4sn+PvawAocYzy+fh9DQC7+x5yiPKJAECFuNUzlY/7PgBUmJWP+z4AVIi+mconAgB7Gu/3RPrycfQGwJ7GI7dIXz6O3gDYy8+QzyGL8onESgQAW5u2nkhfPJFopWgnANjKbOuJ9MXT4vgNgK0siicye9PF8RsAWxgfrT7PYvAXx28APGt6tPo86fAvCgiAR6XHbS3psIsCAuBeV4snkg7PooAAWCO6Ih6pvlo8kXSYJH5R/EIlBEDm5rbTJx1eiS0IgHPxYMHq4omkwxuxBQEQonTSR6lvJR2uTCsh/xME8D7afZ2HSqclHT6QuIi4GGUE8H9pZdNy1/HapaTDDdKXkYiIvG42KZt5Tod/OGkUGYvStAgAAAAASUVORK5CYII=',
        border: 5,
        x: 300,
        y: 300,
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
    uid: '51',
    api: 'https://vk-donatelo.herokuapp.com'
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
      let resp = await axios.get(state.api + '/groups_list?uid=' + state.uid);
      console.log(resp);
      commit('setGroups', resp.data);
    },
    async loadGroup({commit, state}, {gid, cb}) {
      let resp = await axios.get(state.api + `/group_info?uid=${state.uid}&gid=${gid}`);
      commit('setGroup', resp.data);
      cb(resp.data);
    },
    async uploadData({comit, state}, data) {
      data.uid = state.uid;
      console.log(data);
      let resp = await axios.post(state.api + '/update_group', data);
    },
    async removeGroup({commit, state}, gid) {
      let resp = await axios.post(state.api + '/remove_group', {gid, uid: state.uid});
      commit('removeGroup', gid);
    }
  }
}
