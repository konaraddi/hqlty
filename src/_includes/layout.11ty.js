exports.render = function (data) {
  const isHomepage = data.page.url === "/";

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${data.title || 'odap'}</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header>
    <h1>online discourse anti-patterns</h1>
    <nav>
      <a href="/">Home</a> / <a href="/about/">About</a> / <a href="https://github.com/konaraddi/odap" target="_blank" rel="noopener noreferrer">Github</a>
    </nav>
  </header>

  <main>
    ${isHomepage ? data.content : `
    <article>
      <h1>${data.title}</h1>
      ${data.content}
    </article>
    `}
  </main>
</body>
</html>`;
};
