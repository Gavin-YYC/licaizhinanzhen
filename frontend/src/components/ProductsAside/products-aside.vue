<template lang="html">
  <aside class="products__slide">
    <form @change="handleFormChange">
      <div class="form-control">
        <label for="invest" class="form-control__label"><i class="iconfont icon-class"></i> 所属分类</label>
        <div class="form-control__content">
          <span
            class="form-control__span"
            v-for="item, id in types"
            :class="{active: id == activeFilterTypeIndex}"
            @click.prevent="handleFilterTypeClick(id)">{{item}}</span>
        </div>
      </div>
      <div class="form-control">
        <label class="form-control__label"><i class="iconfont icon-status"></i> 状态</label>
        <div class="form-control__content">
          <span
            class="form-control__span"
            v-for="item, id in biddingStatusStatus"
            :class="{active: id == activeFilterStatusIndex}"
            @click.prevent="handleFilterStatusClick(id)">{{item}}</span>
        </div>
      </div>
      <div class="form-control">
        <label class="form-control__label"><i class="iconfont icon-threshold"></i> 投资门槛</label>
        <div class="form-control__group">
          从：<input type="text" class="form-control__item" name="" v-model="investmentThreshold.value[0]">
          到：<input type="text" class="form-control__item" name="" v-model="investmentThreshold.value[1]">
        </div>
      </div>
      <div class="form-control">
        <label class="form-control__label"><i class="iconfont icon-profit"></i> 预期年化收益率</label>
        <vue-slider v-model="annualRateData.value" v-on:drag-end="getContent" v-bind="annualRateData"></vue-slider>
        <div class="form-control__output">
          <span>最高: {{annualRateData.value[0]}}</span>
          <span>最低: {{annualRateData.value[1]}}</span>
        </div>
      </div>
      <div class="form-control" v-if="activeFilterTypeIndex != 1">
        <label class="form-control__label"><i class="iconfont icon-cycle"></i> 投资周期</label>
        <vue-slider v-model="investmentCycleData.value" v-on:drag-end="getContent" v-bind="investmentCycleData"></vue-slider>
      </div>
      <div class="form-control">
        <label class="form-control__label"><i class="iconfont icon-risk"></i> 风险级别</label>
        <vue-slider v-model="investmentRiskLevelData.value" v-on:drag-end="getContent" v-bind="investmentRiskLevelData"></vue-slider>
      </div>
      <div class="form-control">
        <label class="form-control__label"><i class="iconfont icon-process"></i> 招标进度</label>
        <vue-slider v-model="biddingProgressData.value" v-on:drag-end="getContent" v-bind="biddingProgressData"></vue-slider>
        <div class="form-control__output">
          <span>最高: {{biddingProgressData.value[0]}}</span>
          <span>最低: {{biddingProgressData.value[1]}}</span>
        </div>
      </div>
      <div class="form-control form-control--horizon">
        <label class="form-control__label"><i class="iconfont icon-authority"></i> 银行资金存款</label>
        <my-checkbox v-on:change="handleChange" :selected="bankDeposit"></my-checkbox>
      </div>
    </form>
  </aside>
</template>

<script>

import vueSlider from 'vue-slider-component';
import MyCheckbox from '../ui/checkbox/checkbox.vue';

export default {
  name: 'ProductsAside',

  components: {
    vueSlider,
    MyCheckbox
  },

  data() {
    return {}
  },

  computed: {
    activeFilterTypeIndex() { return this.$store.state.asideData.activeFilterTypeIndex },
    activeFilterStatusIndex() { return this.$store.state.asideData.activeFilterStatusIndex },
    types () { return this.$store.state.asideData.types },
    biddingStatusStatus () { return this.$store.state.asideData.biddingStatusStatus },
    investmentThreshold () { return this.$store.state.asideData.investmentThreshold },
    annualRateData () { return this.$store.state.asideData.annualRateData },
    investmentCycleData () { return this.$store.state.asideData.investmentCycleData },
    investmentRiskLevelData () { return this.$store.state.asideData.investmentRiskLevelData },
    biddingProgressData () { return this.$store.state.asideData.biddingProgressData },
    bankDeposit () { return Boolean(this.$store.state.asideData.bankDeposit) }
  },

  methods: {
    handleFilterTypeClick ( id ) {
      this.$store.dispatch('setActiveTypeIndex', id);
      this.getContent();
    },
    handleFilterStatusClick ( id ) {
      this.$store.dispatch('setActiveStatusIndex', id);
      this.getContent();
    },
    handleChange( ev ) {
      this.$store.dispatch('setActiveBankDeposit', ev.target.checked);
    },
    handleFormChange( ev ) {
      this.getContent();
    },

    getContent() {
      const that = this;
      const POST_DATA = {
        type: that.type,
        status: that.status,
        threshould: JSON.stringify(that.threshould),
        profitRate: JSON.stringify(that.profitRate),
        cycle: JSON.stringify(that.cycle),
        riskLevel: JSON.stringify(that.riskLevel),
        process: JSON.stringify(that.process),
        bankDeposit: that.bankDeposit
      };
      this.$store.dispatch('getProductList', POST_DATA);
    }
  }
}
</script>

<style lang="less">
.products__slide {
  width: 23%;
  border-right: 1px solid #ddd;
  padding-right: 10px;
}
.form-control {
  color: rgba(0,0,0,.65);
  vertical-align: top;
  position: relative;
  padding: 0 0 30px 0;
  display: block;
}
.form-control:hover .form-control__label {
  color: #1da1fd;
}
.form-control__label {
  padding: 0 0 8px;
  display: block;
  text-align: left;
  transition: all ease 0.4s;
}
.form-control--horizon {
  display: flex;
  justify-content: space-between;
}
.form-control__span {
  margin-right: 8px;
  font-size: 12px;
  font-weight: 400;
  margin-bottom: 12px;
  background: #fff;
  border-radius: 5px;
  padding: 4px 15px;
  border: 1px dashed #d9d9d9;
  cursor: pointer;
  white-space: nowrap;
  transition: all ease 0.4s;
}
.form-control__span.active {
  background: #1da1fd;
  color: #fff;
}
.form-control__span:hover {
  border-color: #1da1fd;
}
.form-control__output {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  padding: 4px 8px 0 8px;
}
.form-control__group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
}
.form-control__item {
  width: 30%;
  color: rgba(0,0,0,.65);
  border: 1px solid #d9d9d9;
  background-color: #fff;
  border-radius: 4px;
  transition: all .3s;
  padding: 4px 7px;
  display: inline-block;
}
.form-control__item:hover {
  border-color: #49a9ee;
}
.form-control__item:focus {
  border-color: #49a9ee;
  box-shadow: 0px 0px 3px 0px #49a9ee;
}
.form-control__content {
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
}
</style>
