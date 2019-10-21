const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const config = require('./webpack.base.config.js');

config.mode = 'production';

config.output.path = require('path').resolve('./data/static/dist')

config.plugins = config.plugins.concat([
  new BundleTracker({ filename: './webpack-stats-prod.json' }),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('production')
    }
  }),

  // keeps hashes consistent between compilations
  new webpack.optimize.OccurrenceOrderPlugin(),
]);

config.optimization.minimize = true;
// Add a loader for JSX files
// config.module.loaders.push(
//   { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel' }
// )


module.exports = config;
