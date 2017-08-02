<template lang="html">
  <div class="wrap">
    <!--Header-->
    <my-header></my-header>

    <!--新手标-->
    <my-title-bar :title="titles[0]" v-on:click="handleClick"></my-title-bar>
    <section class="freshman__container">
      <my-card :list="productForNewList"></my-card>
    </section>

    <!--分类搜索-->
    <my-title-bar :title="titles[1]"></my-title-bar>
    <section class="products__container">
      <products-aside></products-aside>
      <products-content :list="productList"></products-content>
    </section>

    <!--理财产品-->
    <my-title-bar :title="titles[2]"></my-title-bar>
    <section class="compony__container">
      <div class="componies">
        <my-compony v-for="item in componyList" :data="item"></my-compony>
      </div>
    </section>

    <!--Footer-->
    <my-footer></my-footer>
  </div>
</template>

<script>
import MyHeader from './components/header/header.vue';
import MyFooter from './components/footer/footer.vue';
import MyTitleBar from './components/titleBar/title-bar.vue';
import MyCard from './components/card/card.vue';
import ProductsAside from './components/ProductsAside/products-aside.vue';
import ProductsContent from './components/ProductsContent/products-content.vue';
import MyCompony from './components/compony/compony.vue';

export default {

  components: {
    MyHeader,
    MyFooter,
    MyTitleBar,
    MyCard,
    ProductsAside,
    ProductsContent,
    MyCompony
  },

  computed: {
    // 新手标
    productForNewList() {
      return this.$store.state.productForNewList;
    },
    // 产品
    productList() {
      return this.$store.state.productList;
    },
    // 理财产品
    componyList() {
      return this.$store.state.componyList;
    }
  },

  data: function () {
    return {
      titles: [
        "新手标",
        "分类查询",
        "理财产品"
      ]
    }
  },

  created() {
    // 获取新手标数据
    this.$store.dispatch('getFreshmanList');
    // 获取分类搜索数据
    this.$store.dispatch('getProductList');
    // 获取公司app数据
    this.$store.dispatch('getComponyList');
  },

  methods: {
    handleClick( ev ) {
      console.log("111");
    }
  }
}
</script>

<style lang="less">
@import "./lib/less/reset.less";
@import "./lib/less/define.less";
body {
  background-color: #f1f3f6;
}
.wrap {
  padding: 0 50px;
  margin-top: 100px;
  min-width: 1200px;
}
.freshman__container {}
.compony__container {}
.products__container {
  .displayFlexRow;
  margin-bottom: 30px;
}
.componies {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
</style>
