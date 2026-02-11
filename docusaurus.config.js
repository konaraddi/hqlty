import { themes as prismThemes } from 'prism-react-renderer';

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
            type: 'docSidebar',
            sidebarId: 'patternsSidebar',
            label: 'Patterns',
            position: 'left',
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
