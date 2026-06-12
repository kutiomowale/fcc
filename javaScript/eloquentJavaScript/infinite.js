#!/usr/bin/env node
function egg() {
  return chicken();
}
function chicken() {
  return egg();
}
console.log(chicken() + " came first.");
