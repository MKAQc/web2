export default {
  content: ["./index.html", "./src/**/*.{js,ts}"],
  theme: {
    extend: {
      colors: {
        primary: "#6366f1", // Twój kolor
      },
    },
  },
  plugins: [],
}

import dayjs from "dayjs"

document.querySelector("#app").innerHTML = `
  <h1 class="text-2xl font-bold text-primary">Kalkulator dni życia</h1>

  <form id="form">
    <input type="date" id="date" />
    <button class="bg-blue-300 p-4">Submit</button>
  </form>

  <dialog id="dialog" class="bg-gray-200">
    <button id="close">X</button>
    <p id="result" class="text-red-600"></p>
  </dialog>
`

const form = document.getElementById("form")
const input = document.getElementById("date")
const dialog = document.getElementById("dialog")
const result = document.getElementById("result")
const closeBtn = document.getElementById("close")

form.addEventListener("submit", (e) => {
  e.preventDefault()

  const birth = dayjs(input.value)
  const today = dayjs()

  const days = today.diff(birth, "day")

  if (birth.date() === today.date() && birth.month() === today.month()) {
    alert("Wszystkiego najlepszego! 🎉")
  }

  result.textContent = `Minęło dni: ${days}`
  dialog.showModal()
})

closeBtn.addEventListener("click", () => {
  dialog.close()
})
