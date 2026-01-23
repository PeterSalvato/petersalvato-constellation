/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './_layouts/**/*.html',
    './_includes/**/*.html',
    './index.html',
    './**/*.md',
  ],
  theme: {
    extend: {
      colors: {
        // Paper and Ink
        'ink': '#1A1A1A',
        'ink-soft': '#2A2A2A',
        'paper': '#F4F4F0',
        'paper-dark': '#EFEFEB',
        'grid': '#E5E5E0',
        'grid-light': '#F0F0EB',

        // Domain Colors (Faded, Technical)
        'domain-blue': '#3A5F85',
        'domain-red': '#A64B2A',
        'domain-green': '#6B8E5F',

        // Accent
        'accent': '#FF4400',
      },
      fontFamily: {
        'sans': ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
        'serif': ['EB Garamond', 'Caslon', 'Georgia', 'serif'],
        'mono': ['Space Mono', 'Courier Prime', 'monospace'],
      },
      fontSize: {
        'xs': '10px',
        'sm': '12px',
        'base': '14px',
        'lg': '16px',
        'xl': '20px',
        '2xl': '24px',
        '3xl': '32px',
        '4xl': '48px',
      },
      letterSpacing: {
        'tight': '-0.04em',
        'normal': '0em',
        'wide': '0.04em',
        'wider': '0.08em',
      },
      lineHeight: {
        'tight': '1.1',
        'normal': '1.5',
        'relaxed': '1.8',
      },
      spacing: {
        'xs': '4px',
        'sm': '8px',
        'md': '16px',
        'lg': '24px',
        'xl': '32px',
        '2xl': '48px',
        '3xl': '64px',
      },
      borderWidth: {
        'DEFAULT': '1px',
        '0': '0',
        '1': '1px',
        '2': '2px',
        '4': '4px',
      },
      maxWidth: {
        'content': '960px',
      },
    },
  },
  plugins: [],
};
