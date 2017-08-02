<template lang="html">
  <div class="products__content">
    <table class="products__table">
      <thead>
        <th class="products__item products__item-head">
          <!-- <td class="products__cell products__cell-checkbox"><my-checkbox v-on:change="handleCheckAll"></my-checkbox></td> -->
          <td class="products__cell products__cell-logo">logo</td>
          <td class="products__cell products__cell-app">APP</td>
          <td class="products__cell products__cell-name">产品名称</td>
          <td class="products__cell products__cell-rate">收益率</td>
          <td class="products__cell products__cell-cycle">投资期限</td>
          <td class="products__cell products__cell-threshold">起投金额</td>
          <td class="products__cell products__cell-process">进度</td>
          <td class="products__cell products__cell-operate">描述</td>
        </th>
      </thead>
      <tbody>
        <template v-if="list.length !== 0">
          <tr class="products__item" v-for="item in list">
            <!-- <td class="products__cell products__cell-checkbox"><my-checkbox :selected="isSelected"></my-checkbox></td> -->
            <td class="products__cell products__cell-logo"><img class="common__icon-img" :src="item.app_icon_src" alt=""></td>
            <td class="products__cell products__cell-app">{{item.app_name}}</td>
            <td class="products__cell products__cell-name">{{item.name}}</td>
            <td class="products__cell products__cell-rate"><span class="products__cell-rate--active">{{item.yield_rate}}</span>%</td>
            <td class="products__cell products__cell-cycle">
              <template v-if="item.type == 1">
                {{item.desc}}
              </template>
              <template v-else>
                {{item.cycle}}天
              </template>
            </td>
            <td class="products__cell products__cell-threshold">{{item.threshold}}元</td>
            <td class="products__cell products__cell-process">{{Number(item.process).toFixed(2)}}%</td>
            <td class="products__cell products__cell-operate">
              <a :href="item.source_url" class="products__cell-btn--view" target="_blank">查看</a> 添加对比</td>
          </tr>
        </template>
        <template v-else>
          <p class="products__empty">该查询条件下没有内容，请修改查询条件后重试吧~</p>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script>
import MyCheckbox from '../ui/checkbox/checkbox.vue';
export default {
  name: 'ProductesContent',

  props: {
    list: {
      type: Array,
      default() {
        return [];
      }
    }
  },

  data() {
    return {
      isSelected: true
    }
  },

  components: {
    MyCheckbox
  },

  methods: {
    handleCheckAll( ev ) {
      this.isSelected = ev.target.checked;
    }
  }
}
</script>

<style lang="less">
@import "../../lib/less/define.less";
.animation-loop(@n, @i:1) when (@i <= @n) {
  .products__item:nth-of-type(@{i}) {
    animation-delay: 0.15s * (@i - 1);
  }
  .animation-loop(@n, (@i + 1));
}
.products__content {
  width: 72%;
}
.common__icon-img {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  background: #fff;
  display: block;
}
.products__table {
  width: 100%;
}
.products__item {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  text-align: left;
  font-size: 14px;
  padding: 10px 20px 10px 20px;
  border-radius: 5px;
  margin: 5px 0;
  background-color: #f7f9fa;
  position: relative;
  transition: all 0.3s ease;
  border-bottom: 1px solid @borderColor;
  box-sizing: border-box;
  animation: fadeInItem 0.3s ease-out both;
  &:hover {
    background: #fff;
    box-shadow: 0px 3px 5px 0px rgba(0, 0, 0, 0.2);
  }
}
.animation-loop(10);
.products__item-head {
  font-weight: normal;
  background: #fff;
  box-shadow: 0px 3px 5px 0px rgba(0, 0, 0, 0.2);
}
.products__cell {
  display: block;
  vertical-align: middle;
  overflow: hidden;
  text-overflow: ellipsis;
}
.products__empty {
  text-align: center;
  padding: 30px;
}
.products__cell-checkbox {
  width: 50px;
}
.products__cell-logo {
  width: 80px;
}
.products__cell-app {
  width: 150px;
}
.products__cell-name {
  width: 150px;
}
.products__cell-rate {
  color: #ff2c3c;
  width: 80px;
  text-align: center;
}
.products__cell-cycle {
  width: 100px;
  text-align: center;
}
.products__cell-threshold {
  width: 100px;
}
.products__cell-process {
  width: 80px;
}
.products__cell-rate--active {
  font-size: 24px;
  font-weight: 500;
}
.products__item-head {
  animation: none;
  opacity: 1;
  .products__cell-rate {
    color: inherit;
  }
}
@keyframes fadeInItem {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
</style>
