const body = document.querySelector("body");
const green = document.querySelector(".green");
const red = document.querySelector(".red");
const black = document.querySelector(".black");

green.addEventListener("click", () => {
  if (body.style.backgroundColor !== "green") {
    body.style.backgroundColor = "green";
  }
});

red.addEventListener("click", () => {
  if (body.style.backgroundColor !== "red") {
    body.style.backgroundColor = "red";
  }
});

black.addEventListener("click", () => {
  if (body.style.backgroundColor !== "black") {
    body.style.backgroundColor = "black";
  }
});
