import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue2"
import { viteSingleFile } from "vite-plugin-singlefile"
import path from "path";

export default defineConfig({
  plugins: [vue(), viteSingleFile()],
  base: "./",
  root: "./",
  alias: {
    // 键必须以斜线开始和结束
    '/@/': path.resolve(__dirname, './src'),
    // 'vue$': 'vue/dist/vue.runtime.esm-bundler.js',
  },
  build: {
    outDir: "gui",
    emptyOutDir: true,
  }
})