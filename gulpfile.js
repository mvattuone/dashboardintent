'use strict';

// Add all scripts to at least a /scripts/ dir so we can run watch against all files

var browserify = require('browserify'),
    gulp = require('gulp'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    gutil = require('gulp-util'),
    uglify = require('gulp-uglify'),
    sourcemaps = require('gulp-sourcemaps');

gulp.task('javascript', function () {
  // set up the browserify instance on a task basis
  var b = browserify({
    entries: 'CI_Dash/static/js/main.js',
    debug: true,
  })

  return b.bundle()
    .on('error', function() {
      gutil.log();
      this.emit('end');
    })
    .pipe(source('CI_Dash/static/js/bundle.js'))
    .on('error', function() {
      gutil.log();
      this.emit('end');
    })
    .pipe(buffer())
    .on('error', function() {
      gutil.log();
      this.emit('end');
    })
    .pipe(sourcemaps.init({loadMaps: true}))
    .on('error', function() {
      gutil.log();
      this.emit('end');
    })
    .pipe(sourcemaps.write('./'))
    .on('error', function() {
      gutil.log();
      this.emit('end');
    })
    .pipe(gulp.dest('.'));
});

gulp.task('watch', function() { 
  gulp.watch(['CI_Dash/static/js/*'], ['javascript']);
});