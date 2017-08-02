<template lang="html">
  <section class="common__title">
    <span class="common__title--text">{{title}} <small>以下产品来自活动方，不构成推荐建议，参考收益不代表实际收益，请谨慎参与活动</small></span>
    <span class="common__title--showmore" @click="handleClick">查看更多>></span>
  </section>
</template>

<script>
export default {

  name: 'MyTitleBar',

  props: {
    title: {
      type: String,
      default: '标题'
    }
  },

  methods: {
    handleClick( ev ) {
      this.$emit('click', ev);
    }
  }
}
</script>

<style lang="less">
.common__title {
  height: 60px;
  line-height: 60px;
  position: relative;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #ddd;
  margin-bottom: 30px;
}
.common__title--text small {
  font-size: 12px;
}
.common__title--text::before {
  content: "◎";
  width: 20px;
  display: inline-block;
}
.common__title--showmore {
  cursor: pointer;
  transition: all ease 0.3s;
  &:hover {
    color: #1da1fd;
  }
}
</style>
