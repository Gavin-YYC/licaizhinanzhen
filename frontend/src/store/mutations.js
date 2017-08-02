export default {
  setFreshmanList(state, payload) {
    state.productForNewList = payload;
  },

  setProductList(state, payload) {
    state.productList = payload;
  },

  setComponyList(state, payload) {
    state.componyList = payload;
  },

  setActiveTypeIndex( state, payload ) {
    state.asideData.activeFilterTypeIndex = payload;
  },

  setActiveStatusIndex( state, payload ) {
    state.asideData.activeFilterStatusIndex = payload;
  },

  setActiveBankDeposit( state, payload ) {
    state.asideData.bankDeposit = payload;
  }
}
