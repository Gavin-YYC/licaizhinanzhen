<template lang="html">
  <label class="checkbox-wrap">
    <span class="checkbox" :class="{'checkbox--checked': value === true}">
      <input type="checkbox" name="" v-model="value" value="" class="checkbox__input" @change="handleChange">
      <span class="checkbox__inner"></span>
    </span>
    <span class="checkbox__label">{{label}}</span>
  </label>
</template>

<script>
export default {
  name: "MyCheckbox",

  props: {
    label: {
      type: String,
      default: ''
    },
    selected: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      value: this.selected
    }
  },

  watch: {
    value(newV, oldV) {
      this.value = newV;
    }
  },

  methods: {
    handleChange( ev ) {
      this.$emit('change', ev);
    }
  }
}
</script>

<style lang="less">
.checkbox-wrap {
  cursor: pointer;
  display: inline-block;
  font-size: 14px;
  user-select: none;
}
.checkbox {
  display: inline-flex;
  position: relative;
  vertical-align: text-bottom;
  line-height: 1;
}
.checkbox__input {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  opacity: 0;
  width: 100%;
  height: 100%;
}
.checkbox__inner {
  position: relative;
  display: block;
  top: 0;
  left: 0;
  width: 14px;
  height: 14px;
  border: 1px solid #d9d9d9;
  border-radius: 2px;
  background-color: #fff;
  transition: all .3s;
}
.checkbox__inner:after {
  transform: rotate(45deg) scale(0);
  position: absolute;
  left: 4px;
  top: 1px;
  display: table;
  width: 5px;
  height: 8px;
  border: 2px solid #fff;
  border-top: 0;
  border-left: 0;
  content: " ";
  transition: all .1s cubic-bezier(.71,-.46,.88,.6);
}
.checkbox--checked .checkbox__inner {
  background-color: #108ee9;
  border-color: #108ee9;
}
.checkbox--checked .checkbox__inner:after {
  transform: rotate(45deg) scale(1);
  position: absolute;
  left: 4px;
  top: 1px;
  display: table;
  width: 5px;
  height: 8px;
  border: 2px solid #fff;
  border-top: 0;
  border-left: 0;
  content: " ";
  transition: all .2s cubic-bezier(.12,.4,.29,1.46) .1s;
}
.checkbox__label {

}
</style>
