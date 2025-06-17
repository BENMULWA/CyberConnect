/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './homepage/templates/blog/**/*.html',
    './src/**/*.js',
    './src/**/*.css',
  ],
   safelist: [
    'left-[0]',
    'left-[-100%]',
   ],
  theme: {
    screens: {
      sm: "340px",
      md: "540px",
      lg: "768px",
      xl: "1180px"
    },
    extend: {
      fontFamily: {  //fixed from fontfamily to fontFamily
        Roboto: ["Roboto Mono", "monospace"],
        Lobster: ["Lobster", "sans-serif"],
        jost: ["Jost", "sans-serif"]
      },
      container: {
        center: true,
        padding: {
          DEFAULT: "12px",  //use DEFAULT (not "default") for global default padding
          md: "32px"
        }
      },
    }
  },
  plugins: [],
}


//background

module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/static/images/bg.jpg')",
      },
    },
  },
};
