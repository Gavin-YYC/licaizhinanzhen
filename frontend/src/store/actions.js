import Api from '../apis/api';
import state from './state.js';
import formatCenter from './format_center.js';

const format = new formatCenter();

let $http;

export default {
  use( vue ) {
    $http = vue.http;
  },

  getFreshmanList({commit}) {
    return new Promise((resolve, reject) => {
      $http.get(Api.freshman.list).then( res => {
        const result = res.data;
        if ( result.ret === 0 ) {
          resolve( result.content );
          commit('setFreshmanList', result.content || []);
        } else {
          reject( res.data.msg );
        }
      }, error => {
        reject( error );
      });
    });
  },

  getProductList({commit}) {
    const asideData = state.asideData;
    const payload = {
      type: asideData.activeFilterTypeIndex,
      status: asideData.activeFilterStatusIndex,
      threshould: JSON.stringify(asideData.investmentThreshold.value),
      profitRate: JSON.stringify(asideData.annualRateData.value),
      cycle: JSON.stringify(format.formatInvestmentCycle(asideData.investmentCycleData.value)),
      riskLevel: JSON.stringify(format.formatRiskLevel(asideData.investmentRiskLevelData.value)),
      process: JSON.stringify(asideData.biddingProgressData.value),
      bankDeposit: Number(asideData.bankDeposit)
    }
    return new Promise((resolve, reject) => {
      $http.get(Api.product.list, {
        params: payload || {}
      }).then( res => {
        const result = res.data;
        if ( result.ret === 0 ) {
          resolve( result.content );
          commit('setProductList', result.content || []);
        } else {
          reject( res.data.msg );
        }
      }, error => {
        reject( error );
      });
    });
  },

  getComponyList({commit}) {
    return new Promise((resolve, reject) => {
      $http.get(Api.app.list).then( res => {
        const result = res.data;
        if ( result.ret === 0 ) {
          resolve( result.content );
          commit('setComponyList', result.content || []);
        } else {
          reject( res.data.msg );
        }
      }, error => {
        reject( error );
      });
    });
  },

  // 产品过滤
  getFilterContent({commit}, payload) {
    console.log( payload );
  },

  setActiveTypeIndex({commit}, payload) {
    commit('setActiveTypeIndex', payload);
  },

  setActiveStatusIndex({commit}, payload) {
    commit('setActiveStatusIndex', payload);
  },

  setActiveBankDeposit({commit}, payload) {
    commit('setActiveBankDeposit', payload);
  }
}
