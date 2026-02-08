module.exports = function (eleventyConfig) {
  // Copy static assets
  eleventyConfig.addPassthroughCopy("src/static");

  // Sorted patterns collection: by priority (high > medium > low), then alphabetically by title
  const priorityOrder = { high: 0, medium: 1, low: 2 };
  eleventyConfig.addCollection("patternsByPriority", (collectionApi) => {
    return collectionApi.getFilteredByTag("patterns").sort((a, b) => {
      const pa = priorityOrder[a.data.priority] ?? 1;
      const pb = priorityOrder[b.data.priority] ?? 1;
      if (pa !== pb) return pa - pb;
      return a.data.title.localeCompare(b.data.title);
    });
  });

  return {
    dir: {
      input: "src",
      output: "_site"
    }
  };
};
