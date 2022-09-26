<template>
  <div class="content">
    <a target="_blank" href="http://www.zhangwenbing.com">go to author's blog</a>
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

<style scoped>
</style>