---
title: odap
layout: layout.11ty.js
eleventyExcludeFromCollections: true
---

A reference for online discourse antipatterns: the subtle conversation moves that sound reasonable but derail productive discussion on Reddit, Hacker News, Twitter, and other internet forums.

## anti-patterns

{% for p in collections.patternsByPriority -%}
- [{{ p.data.title }}]({{ p.url }})
{% endfor %}
