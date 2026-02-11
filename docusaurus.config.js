import { themes as prismThemes } from 'prism-react-renderer';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function getPatternNavbarItems() {
  const patternsDir = path.join(__dirname, 'docs', 'patterns');
  return fs
    .readdirSync(patternsDir)
    .filter((f) => f.endsWith('.md') && !f.startsWith('_'))
    .map((f) => {
      const content = fs.readFileSync(path.join(patternsDir, f), 'utf-8');
      const titleMatch = content.match(/^title:\s*(.+)$/m);
      const title = titleMatch ? titleMatch[1].trim() : f.replace('.md', '');
      const slug = f.replace('.md', '');
      return { type: 'doc', docId: `patterns/${slug}`, label: title };
    })
    .sort((a, b) => a.label.localeCompare(b.label));
}

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'online discourse anti-patterns',
  tagline: 'A reference for online discourse antipatterns: the subtle conversation moves that sound reasonable but derail productive discussion.',
  url: 'https://odap.konaraddi.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {},
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'odap',
        items: [
          { type: 'doc', docId: 'index', label: 'About', position: 'left' },
          {
            type: 'dropdown',
            label: 'Patterns',
            position: 'left',
            items: getPatternNavbarItems(),
          },
          { type: 'doc', docId: 'contributing', label: 'Contributing', position: 'left' },
          {
            href: 'https://github.com/konaraddi/odap',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      colorMode: {
        defaultMode: 'light',
        respectPrefersColorScheme: true,
      },
    }),
};

export default config;
