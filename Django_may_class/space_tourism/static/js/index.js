const HOME = document.getElementById("home");
const DESTINATION = document.getElementById("destination");
const CREW = document.getElementById("crew");
const TECHNOLOGY = document.getElementById("technology");
const selection = document.getElementById("selection");
const main = document.querySelector("main");
const BODY = document.querySelector("body");
const subNAV = document.querySelector(".navigate");
const pageNAV = document.querySelectorAll(".navigate button");
const toggleHAMBURGER = document.querySelector(".hamburger");
const navContents = document.querySelector(".nav-bar-contents");

let index;
let activeNavId;
let activeNav;
let timer = 4000;
let loaded = false;

const url = window.location.href;

if (url.includes("home")) {
  navContents.children[0].classList.add("active");
  navContents.children[1].classList.remove("active");
  navContents.children[2].classList.remove("active");
  navContents.children[3].classList.remove("active");
} else if (url.includes("destination")) {
  navContents.children[1].classList.add("active");
  navContents.children[0].classList.remove("active");
  navContents.children[2].classList.remove("active");
  navContents.children[3].classList.remove("active");
} else if (url.includes("crew")) {
  navContents.children[2].classList.add("active");
  navContents.children[0].classList.remove("active");
  navContents.children[1].classList.remove("active");
  navContents.children[3].classList.remove("active");
} else if (url.includes("technology")) {
  navContents.children[3].classList.add("active");
  navContents.children[0].classList.remove("active");
  navContents.children[1].classList.remove("active");
  navContents.children[2].classList.remove("active");
}

console.log(url);

if (url.includes("destination")) {
  fetchDestinations();
} else if (url.includes("crew")) {
  fetchCrew();
} else if (url.includes("technology")) {
  fetchTechnologies();
} else {
  console.log("home page");
}

function fetchCrew() {
  fetch(CREWS_URL)
    .then((res) => res.json())
    .then((data) => {
      if (!BODY.classList.contains("home")) {
        const navBTN = [...subNAV.children];

        console.log(data);
        let btns = [];
        let btnId;
        let timerIntv;
        navBTN.forEach((li) => {
          btns.push(li.children[0]);
        });

        for (let x = 0; x <= 1; x++) {
          if (!loaded) {
            let btn = btns[0];
            btnId = 0;
            switcher();
            loaded = true;
          } else {
            btns.forEach((btn) => {
              if (btn.classList.contains("active")) {
                btnId = btns.indexOf(btn);
                console.log("timer started");
                timerIntv = setInterval(switcher, timer);
              }

              btn.addEventListener("click", () => {
                btnId = btns.indexOf(btn);
                selectJson(btnId, btn);
              });
            });
          }

          function switcher() {
            if (btnId >= btns.length - 1) {
              btnId = 0;
              selectJson(btnId, btns[btnId]);
              // console.log(btns[btnId])
            } else {
              btnId = loaded ? (btnId += 1) : 0;
              selectJson(btnId, btns[btnId]);
              // console.log(btns[btnId - 1])
            }
          }
        }

        function selectJson(index, element) {
          if (BODY.classList.contains("crew")) {
            crewFill(index, element);
          }
        }

        function crewFill(index, element) {
          selection.children[0].innerText = data[index].role;
          selection.children[1].innerText = data[index].name;
          selection.children[2].innerText = data[index].bio;
          selection.previousElementSibling.src = data[index].images.png;
          pageNAV.forEach((btn) => btn.classList.remove("active"));
          element.classList.add("active");
        }
      }
    });
}

function fetchDestinations() {
  fetch(DESTINATIONS_URL)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (!BODY.classList.contains("home")) {
        const navBTN = [...subNAV.children];

        console.log(data);
        let btns = [];
        let btnId;
        let timerIntv;
        navBTN.forEach((li) => {
          btns.push(li.children[0]);
        });
        btns.forEach((btn) => {
          if (btn.classList.contains("active")) {
            btnId = btns.indexOf(btn);
            timerIntv = setInterval(() => {
              if (btnId >= btns.length - 1) {
                btnId = 0;
                selectJson(btnId, btns[btnId]);
                console.log(btns[btnId]);
              } else {
                btnId += 1;
                selectJson(btnId, btns[btnId]);
                console.log(btns[btnId - 1]);
              }
            }, timer);
          }
          btn.addEventListener("click", () => {
            btnId = btns.indexOf(btn);
            selectJson(btnId, btn);
          });
        });

        function selectJson(index, element) {
          // console.log(selection.previousElementSibling.src)
          if (BODY.classList.contains("destination")) {
            selection.children[1].innerText = data[index].name;
            selection.previousElementSibling.src = data[index].images.png;
            selection.children[2].innerText = data[index].description;
            selection.nextElementSibling.children[2].innerText =
              data[index].travel;
            selection.nextElementSibling.children[3].innerText =
              data[index].distance;
            pageNAV.forEach((btn) => btn.classList.remove("active"));
            element.classList.add("active");
          }
        }
      }
    });
}

function fetchTechnologies() {
  fetch(TECHNOLOGIES_URL)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (!BODY.classList.contains("home")) {
        const navBTN = [...subNAV.children];

        let btns = [];
        let btnId;
        let timerIntv;
        navBTN.forEach((li) => {
          btns.push(li.children[0]);
        });
        for (let x = 0; x <= 1; x++) {
          if (!loaded) {
            let btn = btns[0];
            btnId = 0;
            switcher();
            loaded = true;
          } else {
            btns.forEach((btn) => {
              if (btn.classList.contains("active")) {
                btnId = btns.indexOf(btn);
                timerIntv = setInterval(switcher, timer);
              }
              btn.addEventListener("click", () => {
                btnId = btns.indexOf(btn);
                selectJson(btnId, btn);
              });
            });
          }
          function switcher() {
            if (btnId >= btns.length - 1) {
              btnId = 0;
              selectJson(btnId, btns[btnId]);
              // console.log(btns[btnId])
            } else {
              btnId = loaded ? (btnId += 1) : 0;
              selectJson(btnId, btns[btnId]);
              // console.log(btns[btnId - 1])
            }
          }
        }

        function selectJson(index, element) {
          if (BODY.classList.contains("technology")) {
            let width;
            selection.children[1].innerText = data[index].name;
            selection.children[2].innerText = data[index].description;

            if (window.innerWidth <= 640) {
              width = "portrait";
            } else {
              width = "landscape";
            }
            selection.previousElementSibling.src = data[index].images[width];
            pageNAV.forEach((btn) => btn.classList.remove("active"));
            element.classList.add("active");
          }
        }
      }
    });
}

toggleHAMBURGER.addEventListener("click", () => {
  document.querySelector(".nav-bar-contents").classList.toggle("clicked");
  document.querySelector(".hamburger img").classList.toggle("close");

  if (
    !document.querySelector(".nav-bar-contents").classList.contains("clicked")
  ) {
    document.querySelector(".nav-bar-contents").classList.add("unclicked");
    document.querySelector(".hamburger img").src =
      '{% static "images/shared/icon-hamburger.svg" %}';
  } else {
    document.querySelector(".nav-bar-contents").classList.remove("unclicked");
    document.querySelector(".hamburger img").src =
      '{% static "images/shared/icon-close.svg" %}';
  }
});
