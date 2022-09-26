// 导入核心模块 path
const path = require('path')
// 导入自动生成html文件的插件
const HtmlWebpackPlugin = require('html-webpack-plugin')
// 导入自动清除 dist 目录的插件
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
// vue3 npm install -D vue-loader vue-template-compiler
// vue2  vue-loader 不能为 16 以上，vue 版本为 2.6.1 必须 和 vue-template-compiler 2.6.1 一致
const { VueLoaderPlugin } = require('vue-loader')

// 配置文件
module.exports = {
  // 配置入口
  entry: './src/index.js',
  // webpack.config.js 文件 配置出口
  output: {
    filename: 'index.[fullhash:8].js', // 出口文件的名称  'main[hash:8].js' 清除缓存
    path: path.join(__dirname, '/gui') // 出口文件生成的路径
  },
  // 配置 mode, development 开发环境  production 生产环境
  mode: 'development',
  // 配置解析
  resolve: {
    alias: {
      // key: value
      '@': path.join(__dirname, 'src')
    },
    // 配置可省略的后缀
    extensions: ['.js', '.css', '.less', '.vue']
  },
  // 配置源码映射
  // devtool: 'source-map',
  // 配置 loader
  module: {
    // 配置规则
    rules: [
      // * vue配置loader
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      // * 解析css loader
      {
        test: /\.css$/,
        use: [
          "style-loader",
          "css-loader"
        ]
      },

      // * 解析Scss样式  注意： 配置的顺序是反着来的  从大到小 从右到左
      {
        test: /\.s[ca]ss$/,
        use: ['style-loader', 'css-loader', 'sass-loader']
      },
      // * 解析图片 的 loader
      {
        test: /\.(png|jpg|gif|svg|webp|jpeg)$/,
        use: "url-loader"
      },
      //  * 解析es6语法 转换 es5 
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
    ]
  },
  // 配置 plugin
  plugins: [
    // 自动生成html文件的插件
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: path.join(__dirname, './src/index.html')
    }),
    // 自动清除 dist 目录插件
    new CleanWebpackPlugin(),
    // 配置 vue loader 插件
    new VueLoaderPlugin(),
  ],
  // 配置开启服务器的信息
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 8080, // 配置端口号
    open: true, // 自动打开浏览器
    hot: true, // 开启模块的热更新
  },
  performance: {
    hints: false
  }
}
