#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (array, last) {
    return (array = array.concat(last));
  }, []);
};
