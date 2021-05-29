questions = JSON.parse(questionsData);
let question_count = 0;
let points = 0;
totalPoints = questions.length * 10;
sessionStorage.setItem("totalPoints", totalPoints);

window.onload = function () {
console.log("hello");

  show(question_count);

};

function next() {


  // if the question is last then redirect to final page
  if (question_count == questions.length - 1) {3
    sessionStorage.setItem("time", time);
    clearInterval(mytime);
    location.href = "endquiz";
  }
  console.log(question_count);

  let user_answer = document.querySelector("li.option.active").innerHTML;
  // check if the answer is right or wrong
  // console.log("user_answer", user_answer);
  // console.log("coorect answer", questions[question_count].fields.correctOption);
  if (user_answer == questions[question_count].fields.correctOption) {
    points += 10; 
    sessionStorage.setItem("points", points);
  }
  console.log(points);

  question_count++;
  show(question_count);
}

function show(count) {
  let question = document.getElementById("questions");
  // let [first, second, third, fourth] = questions[count].options;
  let [first, second, third, fourth] = [questions[count].fields.optionA, questions[count].fields.optionB, questions[count].fields.optionC, questions[count].fields.optionD];

  question.innerHTML = `
  <h2>Q${count + 1}. ${questions[count].fields.question}</h2>
   <ul class="option_group">
  <li class="option">${first}</li>
  <li class="option">${second}</li>
  <li class="option">${third}</li>
  <li class="option">${fourth}</li>
</ul> 
  `;
  toggleActive();
}

function toggleActive() {
  let option = document.querySelectorAll("li.option");
  for (let i = 0; i < option.length; i++) {
    option[i].onclick = function() {
      for (let i = 0; i < option.length; i++) {
        if (option[i].classList.contains("active")) {
          option[i].classList.remove("active");
        }
      }
      option[i].classList.add("active");
    };
  }
}
  