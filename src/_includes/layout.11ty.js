exports.render = function (data) {
  const isHomepage = data.page.url === "/";

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${data.title || 'hqlty'}</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>

  <main>
    ${isHomepage ? data.content : `
    <article>
      <h1>${data.title}</h1>
      ${data.content}
    </article>
    `}
  </main>

  <footer>
    <p><a href="https://github.com/konaraddi/hqlty">GitHub</a></p>
  </footer>
</body>
</html>`;
};
