#!/usr/bin/node

exports.addMeMaybe = (num, cb) => {
  const newnum = num + 1;
  cb(newnum);
};
