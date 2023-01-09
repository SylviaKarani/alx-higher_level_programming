#!/usr/bin/node

exports.callMeMoby = (x, cb) => {
  for (let i = 0; i < x; i++) {
    cb();
  }
};
