#!/usr/bin/env node
function updateRecords(records, id, prop, value) {
  if (value === '') {
    delete records[id][prop];
  } else if (prop !== 'tracks') {
    records[id][prop] = value;
  } else if (records[id].hasOwnProperty('tracks') === false) {
    records[id]['tracks'] = [value];
  } else {
    records[id]['tracks'].push(value);
  }
  return records;
}
