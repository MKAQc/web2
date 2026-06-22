import { API_URL, API_KEY } from "./config.js";

function loadArticles() {
  fetch(API_URL + "?select=*", {
    headers: {
      apikey: API_KEY,
      Authorization: `Bearer ${API_KEY}`
    }
  })
}
function loadArticles() {
  fetch(API_URL + "?select=*", {
    headers: {
      apikey: API_KEY,
      Authorization: `Bearer ${API_KEY}`
    }
  })
    .then((response) => response.json())
    .then((articles) => {
      articlesDiv.innerHTML = "";

      articles.forEach((article) => {
        const el = document.createElement("article");

        el.innerHTML = `
          <h2>${article.title}</h2>
          <h3>${article.subtitle}</h3>
          
          <address>Autor: ${article.author}</address>
          
          <time datetime="${article.created_at}">
            ${new Date(article.created_at).toLocaleString()}
          </time>
          
          <p>${article.content}</p>
        `;

        articlesDiv.appendChild(el);
      });
    })
    .catch((err) => console.log(err));
}
