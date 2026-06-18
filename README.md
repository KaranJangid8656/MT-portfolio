# Portfolio Website

A clean, responsive portfolio template built with HTML, CSS, and JavaScript.

## Features

- Responsive layout for desktop and mobile
- Dark/light theme toggle with saved preferences
- Multiple color palettes and smooth transitions
- Project showcase, skills section, and contact form
- Easy updates through JavaScript-managed content

## Files

- `index.html` — page layout and sections
- `style.css` — styling, responsive design, and palettes
- `script.js` — dynamic content rendering and interactions
- `Images/` — profile and project images
- `favicon/` — icons and manifest

## Customize

- Update project cards, experience, and skills in `script.js`
- Change palette colors in `style.css`
- Add new sections in `index.html` and update navigation links

## Notes

This portfolio is built for easy customization and clean presentation.

## 📱 Responsive Breakpoints

- **Desktop**: 1024px and above
- **Tablet**: 768px - 1023px
- **Mobile**: 480px - 767px
- **Small Mobile**: Below 480px

## 🚀 Performance Features

- **Lazy Loading**: Images load only when needed
- **Debounced Events**: Optimized scroll and resize handlers
- **CSS Variables**: Efficient theme and palette switching
- **Minimal Dependencies**: Only Font Awesome and EmailJS
- **Optimized Images**: Compressed and properly sized

## 🔌 External Dependencies

- **Font Awesome**: For icons
- **Google Fonts**: Inter font family
- **EmailJS**: Contact form functionality

## 📧 Contact Form Setup

1. **Sign up for EmailJS** at [emailjs.com](https://www.emailjs.com/)
2. **Create a service** (Gmail, Outlook, etc.)
3. **Create an email template**
4. **Update the service and template IDs in `script.js`:**
```javascript
emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", data)
```

## 🎨 Theme & Palette Customization

The portfolio supports both light and dark themes combined with 9 different color palettes. Users can:

- **Toggle themes** using the moon/sun button (🌙/☀️)
- **Switch palettes** using the palette button (🎨)
- **Combinations are saved** automatically in localStorage

### Theme + Palette Combinations

Each palette works with both light and dark themes, giving you **18 total visual combinations**:

- **Light Theme**: 9 palette options
- **Dark Theme**: 9 palette options

### Adding New Themes

1. **Add new theme variables in `style.css`:**
```css
[data-theme="your-theme"] {
    --primary-color: #your-color;
    --background: #your-bg;
    /* ... other variables */
}
```

2. **Update ThemeManager in `script.js`:**
```javascript
toggleTheme() {
    const themes = ['light', 'dark', 'your-theme'];
    const currentIndex = themes.indexOf(this.theme);
    const nextIndex = (currentIndex + 1) % themes.length;
    this.setTheme(themes[nextIndex]);
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Images not loading**: Check file paths in `Images/` folder
2. **Contact form not working**: Verify EmailJS configuration
3. **Theme not persisting**: Check localStorage in browser dev tools
4. **Palette not switching**: Ensure palette button exists and JavaScript is loaded
5. **Mobile menu not working**: Ensure hamburger button exists

### Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **CSS Features**: CSS Grid, Flexbox, CSS Variables
- **JavaScript Features**: ES6+, Intersection Observer, Async/Await

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

---

**Built with ❤️ for showcasing data science and machine learning projects**

**Now with 9 beautiful color palettes to match your style! 🎨**
