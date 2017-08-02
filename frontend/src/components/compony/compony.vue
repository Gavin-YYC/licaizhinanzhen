<template lang="html">
  <div class="compony-wrap">
    <!--公司信息-->
    <header class="compony__header">
      <div class="compony__header-top">
        <figure class="compony__icon">
          <img :src="data.icon_src" alt="" class="compony__img">
          <caption class="compony__name">{{data.name}}<br><small>上线日期：2017年12月12日</small></caption>
        </figure>
        <span class="">关注</span>
      </div>
      <div class="compony__header-bottom">
        <span class="compony__status"><i class="iconfont icon-number"></i> 5个项目</span>
        <span class="compony__status"><i class="iconfont icon-count"></i> 累计：300亿</span>
      </div>
    </header>

    <!--公司发展历程-->
    <section class="compony__content" :class="{'compony__content-showmore': componeyShowMore === true}">
      <my-timeline :data="data.news"></my-timeline>
      <span class="compony__more" @click.prevent="componeyShowMore = true">
        <i class="iconfont icon-more"></i>
      </span>
    </section>

    <!--操作按钮-->
    <footer class="compony__footer">
      <a :href="data.home" target="_blank" class="compony__button"><i class="iconfont icon-view"></i> 查看详情</a>
      <span class="compony__button"><i class="iconfont icon-rss"></i> 关注订阅</span>
    </footer>
  </div>
</template>

<script>

import MyTimeline from '../ui/timeline/timeline.vue';

export default {
  name: "MyCompony",

  props: {
    data: {
      type: Object,
      default() {
        return []
      }
    }
  },

  components: {
    MyTimeline
  },

  data() {
    return {
      componyData: [
        {
          title: "2017.03",
          content: "聚财猫获得春晓天泽A轮融资1亿元"
        }, {
          title: "2017.03",
          content: "聚财猫完成银行存管协议签署"
        }, {
          title: "2017.02",
          content: "聚财猫累计交易额突破300亿元"
        }, {
          title: "2017.01",
          content: "聚财猫与安心财产保险有限公司达成合作，资金交易倒转到用风险由安心保险承保"
        }, {
          title: "2017.01",
          content: "聚财猫荣获“中国互联网金融行业优秀示范企业”"
        }, {
          title: "2016.11",
          content: "聚财猫荣获上海市高新技术企业"
        }
      ],

      componeyShowMore: false
    }
  },

  methods: {
    handleSwitchMore() {
      console.log("ds");
    }
  }
}
</script>

<style lang="less">
@import "../../lib/less/define.less";
.compony-wrap {
  width: 30%;
  margin-bottom: 30px;
  border-radius: 5px;
  background-color: #f7f9fa;
  transition: all ease 0.3s;
  margin-right: 30px;
  &:hover {
    box-shadow: 0 3px 8px 0 rgba(0, 0, 0, .3);
  }
}
.compony__header {
  .displayFlexColumn;
  padding: 10px;
}
.compony__header {
  .compony__icon {
    .displayFlexRow;
    align-items: center;
  }
  .compony__name {
    white-space: nowrap;
    padding-left: 20px;
    text-align: left;
  }
  .compony__img {
    width: 60px;
    height: 60px;
    border-radius: 100%;
    background: #fff;
  }
  .compony__header-top,
  .compony__header-bottom {
    .displayFlexRow;
  }
  .compony__header-bottom {
    width: 100%;
    padding-top: 20px;
    justify-content: space-around;
  }
  .compony__status {
    width: 35%;
    font-size: 14px;
    text-align: center;
    line-height: 30px;
    border-radius: 20px;
    border: 1px solid @borderColor;
    vertical-align: middle;
    background: #fff;
    color: #a5b4bb;
    .iconfont {
      color: @mainColor;
      font-weight: 500;
      font-size: 18px;
      vertical-align: middle;
    }
  }
}
.compony__footer {
  .displayFlexRow;
  align-items: center;
  text-align: center;
  padding: 0 10px;
  .compony__button {
    width: 50%;
    line-height: 50px;
    cursor: pointer;
    transition: all ease 0.3s;
    &:first-child {
      margin-left: -1px;
      border-right: 1px solid @borderColor;
    }
    &:hover {
      color: @mainColor;
    }
  }
}
.compony__content {
  height: 200px;
  background: #fff;
  overflow: hidden;
  position: relative;
}
.compony__content-showmore {
  overflow-y: scroll;
  overflow-x: hidden;
  .compony__more {
    display: none;
  }
}
.compony__more {
  position: absolute;
  left: 0;
  bottom: 0;
  line-height: 30px;
  background-color: rgba(255, 255, 255, 0.9);
  width: 100%;
  font-size: 12px;
  text-align: center;
  cursor: pointer;
}
</style>
