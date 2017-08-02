class formatCenter {
  constructor() {

    // 风险级别
    const RISK_LEVEL = {
      '低':   1,
      '中低': 2,
      '中':   3,
      '中高': 4,
      '高':   5
    }

    // 投资周期
    // 将月份转成天数
    // 后端只存储天数
    const INVESTMENT_CYCLE = {
      '7天': 7,
      '1月': 30,
      '3月': 90,
      '6月': 180,
      '9月': 270,
      '12月': 360,
      '>12月': 100000000
    }

    this.RISK_LEVEL = RISK_LEVEL;
    this.INVESTMENT_CYCLE = INVESTMENT_CYCLE;

  }

  formatRiskLevel( riskLevelArr ) {
    if ( riskLevelArr && 'length' in riskLevelArr && riskLevelArr.length === 2 ) {
      return [
        this.RISK_LEVEL[riskLevelArr[0]],
        this.RISK_LEVEL[riskLevelArr[1]]
      ]
    } else {
      return [];
    }
  }

  formatInvestmentCycle( investmentCycleArr ) {
    if ( investmentCycleArr && 'length' in investmentCycleArr && investmentCycleArr.length === 2 ) {
      return [
        this.INVESTMENT_CYCLE[ investmentCycleArr[0] ],
        this.INVESTMENT_CYCLE[ investmentCycleArr[1] ]
      ]
    } else {
      return [];
    }
  }
}

export default formatCenter;
