<template lang="html">
  <ul class="timeline__list">
    <li class="timeline__item" v-for="item in data">
      <span class="timeline__line"></span>
      <span class="timeline__title">{{item.date | timeformat}}</span>
      <span class="timeline__content">{{item.title}}</span>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'MyTimeline',

  props: {
    data: {
      type: Array,
      default() {
        return [];
      }
    }
  },

  filters: {
    timeformat( stamp ) {
      if ( !stamp ) {
        return ''
      }
      function format( num ) {
        if ( num < 10 ) {
          num = '0' + num;
        }
        return num;
      }
      const js_time = new Date( stamp * 1000 );
      const year = js_time.getFullYear() + '.';
      const month = format((js_time.getMonth() + 1))
      return year + month;
    }
  }

  // data格式
  /*
    data = [
      {
        title: "",
        content: ""
      }, {
        title: "",
        content: ""
      }
    ]
  */
}
</script>

<style lang="less">
@import "../../../lib/less/define.less";
.timeline__list {
  padding: 25px;
  .timeline__item {
    font-size: 14px;
    min-height: 20px;
    .displayFlexRow;
    flex-wrap: nowrap;
    justify-content: flex-start;
    position: relative;
    &:last-child {
      .timeline__line {
        border: none;
        &:before {
          left: -6px;
        }
      }
    }
    &:nth-of-type(1) {
      .timeline__line:before {
        border-color: #f5c823;
      }
    }
    &:nth-of-type(2) {
      .timeline__line:before {
        border-color: #ff648c;
      }
    }
    &:nth-of-type(3) {
      .timeline__line:before {
        border-color: #08daa9;
      }
    }
  }
  .timeline__line {
    position: absolute;
    left: 5px;
    top: 0;
    height: 100%;
    border-left: 2px solid #e9e9e9;
    &:before {
      content: "";
      position: absolute;
      top: 0;
      left: -8px;
      width: 12px;
      height: 12px;
      border-radius: 100px;
      background-color: #fff;
      border: 2px solid #108ee9;
      color: #108ee9;
    }
  }
  .timeline__content {
    padding-bottom: 20px;
    position: relative;
    top: -2px;
  }
  .timeline__title {
    padding-left: 25px;
    padding-right: 10px;
    position: relative;
    top: -2px;
  }
}
</style>
