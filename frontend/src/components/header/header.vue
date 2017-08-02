<template lang="html">
  <header class="header">
    <nav class="header__nav">
      <a href="#" class="header__logo"></a>
      <ul class="header__list">
        <a v-for="item in nav"
          :href="item.id" class="header__item"
          :class="{'header__item--active': item.id == activeIndex}"
          @click.prevent="handleClick(item.id)">
          <li class="header__text">{{item.name}}</li>
        </a>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {

  name: 'MyHeader',

  data() {
    return {
      nav: [
        {name: "首页", id: 0},
        {name: "活期", id: 1},
        {name: "定期", id: 2},
        {name: "借贷", id: 3},
        {name: "债务", id: 4},
        {name: "会理财", id: 5}
      ],

      activeIndex: 0
    }
  },

  methods: {
    handleClick: function ( id ) {
      this.activeIndex = id;
    }
  }
}
</script>

<style lang="less">
.header {
  width: 100%;
  height: 80px;
  position: fixed;
  top: 0;
  left: 0;
  padding: 0 50px;
  z-index: 100;
  box-sizing: border-box;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0px 1px 5px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.header__logo {
  background: url('http://img.youthol.top/zhinanzhen_logo.png') center center no-repeat;
  background-size: auto 100%;
  display: block;
  height: 60px;
  width: 200px;
}
.header__list {
  list-style: none;
  display: flex;
  height: inherit;
  justify-content: flex-end;
}
.header__item {
  width: 150px;
  color: #515151;
  line-height: 80px;
  text-align: center;
  transition: all 0.5s ease;
}
.header__item:hover,
.header__item--active {
  color: #1da1fd;
  background: rgba(0, 0, 0, 0.05);
}
.header__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
