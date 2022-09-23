<template>
  <div class="content">
    <a target="_blank" href="http://www.zhangwenbing.com">Skip to author's blog</a>
    <br>
    <button @click="myBtn">Test</button>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    myBtn() {
      console.log(window.pywebview.api.test());
    }
  }
}
</script>

<style>
#app {
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
</style>