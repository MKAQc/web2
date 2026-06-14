const API_URL =
"https://ywophzvskzwpntyrpere.supabase.co/rest/v1/article";

const API_KEY =
"TU_ZOSTAW_SWOJ_OBECNY_KLUCZ";

const articlesDiv = document.getElementById("articles");

loadArticles();

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

```
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
})
.catch((err) => {
  console.log(err);
});
```

}

document
.getElementById("articleForm")
.addEventListener("submit", (e) => {
e.preventDefault();

```
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
```

});
