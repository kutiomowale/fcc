#!/usr/bin/env node
function generatePassword(passwordLength) {
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
  const charsLength = chars.length;
  let password = '';
  for (let i = 0; i < passwordLength; i++) {
    password += chars[Math.floor(Math.random() * charsLength)];
  }
  console.log(`Generated password: ${password}`);
}

generatePassword(8);
