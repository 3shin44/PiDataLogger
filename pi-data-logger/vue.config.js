const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  // for flask templates
  outputDir: '../templates',
  // frontend file apply relative path
  publicPath: "./",
  filenameHashing: false
})
