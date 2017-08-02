/*
 * 全局数据
 *
 */
export default {

  // 侧边栏搜索数据
  asideData: {
    activeFilterTypeIndex: 1,
    activeFilterStatusIndex: 1,

    // 所属分类
    types: {
      1: '活期',
      2: '定期'
      // 3: '债务',
      // 4: '借贷'
    },

    // 银行资金存管
    bankDeposit: false,

    // 预期年化收益率
    annualRateData: {
      value: [3, 10],
      tooltip: "hover",
      min: 0,
      max: 30,
      processStyle: {
        backgroundColor: "#1da1fd"
      }
    },

    // 投资周期
    investmentCycleData: {
      value: ['1月', '3月'],
      tooltip: "hover",
      piecewise: true,
      piecewiseLabel: true,
      data: [ '7天', '1月', '3月', '6月', '9月', '12月', '>12月' ],
      processStyle: {
        backgroundColor: "#1da1fd"
      }
    },

    // 投资门槛
    investmentThreshold: {
      value: [1, 100000]
    },

    // 风险级别
    investmentRiskLevelData: {
      value: ['低', '中'],
      tooltip: "hover",
      piecewise: true,
      piecewiseLabel: true,
      data: [ '低', '中低', '中', '中高', '高' ],
      processStyle: {
        backgroundColor: "#1da1fd"
      }
    },

    // 招标进度
    biddingProgressData: {
      value: [0, 80],
      min: 0,
      max: 100,
      tooltip: "hover"
    },

    // 招标状态
    biddingStatusStatus: {
      1: '募集期',
      2: '收益中',
      3: '售罄',
      4: '异常'
    }
  },

  // 产品列表
  productList: [],

  // 公司列表
  componyList: [],

  // 新手标列表
  productForNewList: []
}
