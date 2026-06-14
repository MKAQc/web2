const API_URL =
  "https://ywophzvskzwpntyrpere.supabase.co/rest/v1/article";

const API_KEY =
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl3b3BoenZza3p3cG50eXJwZXJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA0NzU5ODQsImV4cCI6MjA5NjA1MTk4NH0.G4L_69VWAG7ugSyyP5xDAweBeuzUSWMtBFK-FpsArSk;

const articlesDiv = document.getElementById("articles");

loadArticles();

function loadArticles() {
  fetch(API_URL + "?select=*")
    .then((response) =>
      response.json()
    )
    .then((articles) => {
      articlesDiv.innerHTML = "";

      articles.forEach((article) => {
        articlesDiv.innerHTML += `
          <hr>
          <h2>${article.title}</h2>
          <h3>${article.subtitle}</h3>
          <p><b>Autor:</b> ${article.author}</p>
          <p><b>Data:</b> ${article.created_at}</p>
          <p>${article.content}</p>
        `;
      });
    });
}

document
  .getElementById("articleForm")
  .addEventListener("submit", (e) => {
    e.preventDefault();

    const article = {
      title: document.getElementById("title").value,
      subtitle: document.getElementById("subtitle").value,
      author: document.getElementById("author").value,
      content: document.getElementById("content").value,
    };

    fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        apikey: API_KEY,
        Authorization: `Bearer ${API_KEY}`,
        Prefer: "return=minimal",
      },
      body: JSON.stringify(article),
    }).then(() => {
      loadArticles();
      document.getElementById("articleForm").reset();
    });
  });