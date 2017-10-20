module.exports = {
  state: {
    groups: []
  },
  commits: {
    addGroups(state, data) {
      state.$set('groups', data);
    }
  },
  getters: {
    getGroup(state) {
      
    }
  }
}
