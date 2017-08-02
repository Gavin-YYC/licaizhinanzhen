<template lang="html">
  <footer class="footer">
    <p class="footer__slogan">用心 专业 智能</p>
    <p>投资有风险 入市需谨慎</p>
  </footer>
</template>

<script>
export default {
  name: 'MyFooter'
}
</script>

<style lang="less">
.footer {
  width: 100%;
  z-index: 100;
  box-sizing: border-box;
  line-height: 80px;
  font-size: 16px;
  text-align: center;
  border-top: 1px solid #ddd;
}
.footer__slogan {
  font-size: 40px;
  padding-top: 30px;
}
</style>
