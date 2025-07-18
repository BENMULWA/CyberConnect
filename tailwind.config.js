/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',                 // global templates directory
    './**/templates/**/*.html',              // app-specific templates
    './**/templates/*.html',                 // direct html files
    './src/**/*.{js,ts,jsx,tsx}',            // JS files if using any
  ],

  safelist: [
    'left-[0]',
    'left-[-100%]',
    //'bg-[url("/static/back.png")]',      include this if using dynamic class
  ],

  theme: {
    screens: {
      sm: "340px",
      md: "540px",
      lg: "768px",
      xl: "1180px"
    },
    extend: {
      fontFamily: {
        Roboto: ["Roboto Mono", "monospace"],
        Lobster: ["Lobster", "sans-serif"],
        jost: ["Jost", "sans-serif"]
      },
     /* backgroundImage: {
        bannerImg: "url('/static/back.png')", // named utility class `bg-bannerImg`
      },*/
      container: {
        center: true,
        padding: {
          DEFAULT: "12px",
          md: "32px"
        }
      }
    }
  },

  plugins: [],
}
