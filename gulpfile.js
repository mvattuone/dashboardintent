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
    .on('error', gutil.log)
    .pipe(source('CI_Dash/static/js/bundle.js'))
    .on('error', gutil.log)
    .pipe(buffer())
    .on('error', gutil.log)
    .pipe(sourcemaps.init({loadMaps: true}))
    .on('error', gutil.log)
    .pipe(sourcemaps.write('./'))
    .on('error', gutil.log)
    .pipe(gulp.dest('.'));
});

gulp.task('watch', function() { 
  gulp.watch(['CI_Dash/static/js/*'], ['javascript']);
});