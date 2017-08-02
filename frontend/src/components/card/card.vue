<template lang="html">
  <div class="freshman">
    <div class="freshman__item" v-for="item, index in list" :style="styObj(index)">
      <header class="freshman__header">
        <figure class="freshman__icon">
          <img :src="item.icon" :alt="item.name" class="freshman__img">
          <caption class="freshman__name">{{item.name}}</caption>
        </figure>
        <a :href="item.home_url" target="_blank" class="freshman__button">查看</a>
      </header>
      <footer class="freshman__footer">
        <div class="freshman__profit">
          <span class="freshman__profit--title">收益率</span>
          <span class="freshman__profit--body">{{item.base_yields}}%</span>
        </div>
        <div class="freshman__profit">
          <span class="freshman__profit--title">投资周期</span>
          <span class="freshman__profit--body">{{item.time_long}}天</span>
        </div>
        <div class="freshman__profit">
          <span class="freshman__profit--title">投资门槛</span>
          <span class="freshman__profit--body">{{item.min_invest}}元</span>
        </div>
        <div class="freshman__profit">
          <span class="freshman__ranking">{{index + 1}}</span>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
export default {

  name: 'MyCard',

  props: {
    list: {
      type: Array,
      default: []
    }
  },

  data() {
    return {
      colors: [
        {from: "#64d7f3", to: "#1da1fd"},
        {from: "#89e89a", to: "#44d445"},
        {from: "#e8c8bb", to: "#ff648c"},
        {from: "#e9e679", to: "#f5c823"},
        {from: "#64d7f3", to: "#08daa9"},
        {from: "#e5b0f7", to: "#e84cdc"},
      ],

      styObj: function ( index ) {
        if ( !this.colors[ index ] ) {
          index = 0;
        }
        return {
          background: 'linear-gradient(45deg, ' + this.colors[ index ].from + ', ' + this.colors[ index ].to  + ')'
        }
      }
    }
  }
}
</script>

<style lang="less">
@import "../../lib/less/define.less";
.freshman {
  width: 100%;
  .displayFlexRow;
}
.freshman__item {
  .displayFlexColumn;
  width: 30%;
  height: 200px;
  overflow: hidden;
  box-sizing: border-box;
  margin-bottom: 30px;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0px 1px 1px 0px rgba(0, 0, 0, 0.3);
  transition: all ease 0.3s;
  &:hover {
    box-shadow: 0px 3px 5px 0px rgba(0, 0, 0, 0.5);
  }
}
.freshman__header {
  .displayFlexRow;
}
.freshman__icon {
  position: relative;
  color: #fff;
}
.freshman__img {
  width: 60px;
  height: 60px;
  border-radius: 100%;
  background-color: #fff;
}
.freshman__name {
  position: absolute;
  top: 0;
  left: 80px;
  line-height: 60px;
  white-space: nowrap;
  font-size: 16px;
}
.freshman__button {
  width: 100px;
  height: 50px;
  line-height: 50px;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
  display: block;
  text-align: center;
  border-bottom: 1px solid #fff;
  transition: all 0.1s ease;
}
.freshman__button:hover {
  font-weight: normal;
}
.freshman__footer {
  .displayFlexRow;
}
.freshman__profit .freshman__profit--title {
  font-size: 14px;
}
.freshman__profit .freshman__profit--body {
  font-size: 16px;
}
.freshman__profit .freshman__profit--title,
.freshman__profit .freshman__profit--body {
  display: block;
  text-align: center;
  color: #fff;
}
.freshman__profit:nth-last-child(1) {
  width: 30%;
  position: relative;
}
.freshman__profit .freshman__ranking {
  font-size: 100px;
  font-weight: bold;
  position: absolute;
  top: 0;
  right: 0;
  transform: translateY(-40%);
  color: rgba(255, 255, 255, 0.4);
}
</style>
