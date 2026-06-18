# Muskan's Portfolio - Modern Data Scientist Portfolio

A modern, responsive portfolio website built with HTML, CSS, and JavaScript featuring a clean design, dark/light theme toggle, **9 different color palettes**, and scalable architecture for easy content management.

## 🚀 Features

### Modern Design
- **Clean & Minimalist**: Modern design with excellent typography and spacing
- **Dark/Light Theme**: Toggle between themes with persistent preference
- **9 Color Palettes**: Switch between different color schemes instantly
- **Responsive Design**: Fully responsive across all devices
- **Smooth Animations**: Elegant scroll animations and transitions
- **Loading Screen**: Professional loading experience

### Scalable Architecture
- **Data-Driven Content**: All content managed through JavaScript objects
- **Modular Components**: Easy to add new sections and features
- **Component-Based**: Organized into reusable classes
- **Performance Optimized**: Lazy loading and debounced scroll events

### Interactive Elements
- **Smooth Navigation**: Active section highlighting and smooth scrolling
- **Mobile Menu**: Hamburger menu for mobile devices
- **Contact Form**: Working contact form with EmailJS integration
- **Project Cards**: Interactive project showcase with tags and links
- **Skills Grid**: Categorized skills with hover effects

## 🎨 Color Palette System

The portfolio includes **9 professionally designed color palettes** that you can switch between instantly:

### Available Palettes

1. **Modern Indigo** (Default) - Professional indigo with cyan accents
2. **Minimalist** - Clean grays and neutrals
3. **Tech Blue** - Technology-focused blue with orange accents
4. **Creative** - Bold pink with orange accents
5. **Soft** - Warm orange with pink accents
6. **Nature** - Green with warm orange accents
7. **Corporate** - Professional blue with red accents
8. **Purple** - Modern purple with cyan accents
9. **Sunset** - Warm orange with pink accents

### How to Use Color Palettes

1. **Click the palette button** (🎨) in the top-right corner
2. **Select any palette** from the dropdown menu
3. **Your choice is saved** automatically in localStorage
4. **Works with both light and dark themes**

### Adding Custom Palettes

To add your own color palette:

1. **Add CSS variables** in `style.css`:
```css
[data-palette="your-palette"] {
    --primary-color: #your-color;
    --primary-dark: #your-dark-color;
    --accent-color: #your-accent;
    /* ... other variables */
}
```

2. **Add dark theme variant**:
```css
[data-theme="dark"][data-palette="your-palette"] {
    --primary-color: #your-dark-primary;
    /* ... other dark theme variables */
}
```

3. **Add to HTML dropdown** in `index.html`:
```html
<div class="palette-option" data-palette="your-palette">
    <div class="palette-preview" style="background: linear-gradient(45deg, #your-color, #your-accent);"></div>
    <span>Your Palette</span>
</div>
```

## 📁 Project Structure

```
Website/
├── index.html          # Main HTML structure
├── style.css           # Modern CSS with design system & 9 color palettes
├── script.js           # Modular JavaScript application
├── README.md           # Documentation
└── Images/             # All project images and icons
    ├── Muskan.jpg       # Profile picture
    ├── *.svg           # Skill icons
    └── *.jpg           # Project images
```

## 🎨 Design System

### Color Palette Examples

#### Modern Indigo (Default)
- **Primary**: #6366f1 (Indigo)
- **Accent**: #06b6d4 (Cyan)
- **Perfect for**: Professional tech portfolios

#### Tech Blue
- **Primary**: #2563eb (Blue)
- **Accent**: #f59e0b (Orange)
- **Perfect for**: Software developers, tech companies

#### Creative
- **Primary**: #ec4899 (Pink)
- **Accent**: #f97316 (Orange)
- **Perfect for**: Designers, creative professionals

#### Nature
- **Primary**: #059669 (Green)
- **Accent**: #d97706 (Orange)
- **Perfect for**: Environmental, health, wellness

### Typography
- **Font Family**: Inter (Google Fonts)
- **Font Sizes**: Responsive scale from 0.75rem to 3rem
- **Line Heights**: Optimized for readability

### Spacing
- **Consistent Scale**: 0.25rem to 4rem spacing system
- **Responsive**: Adapts to different screen sizes
- **Component-Based**: Each component has appropriate spacing

## 🔧 How to Add New Content

### Adding New Projects

1. **Edit the `portfolioData.projects` array in `script.js`:**

```javascript
{
    title: 'Your Project Title',
    description: 'Project description here...',
    image: 'Images/your-project-image.jpg',
    tags: ['Python', 'Machine Learning', 'Data Analysis'],
    links: [
        { name: 'View Project', url: 'https://your-project-url.com', icon: 'fas fa-external-link-alt' },
        { name: 'GitHub', url: 'https://github.com/your-repo', icon: 'fab fa-github' }
    ]
}
```

### Adding New Experience

1. **Edit the `portfolioData.experience` array in `script.js`:**

```javascript
{
    title: 'Your Job Title',
    company: 'Company Name',
    date: 'Start Date - End Date',
    description: 'Detailed description of your role and achievements...'
}
```

### Adding New Skills

1. **Edit the `portfolioData.skills` object in `script.js`:**

```javascript
skills: {
    programming: [
        { name: 'New Language', icon: 'Images/new-language.svg' }
    ],
    ml: [
        { name: 'New ML Tool', icon: 'Images/new-ml-tool.svg' }
    ],
    cloud: [
        { name: 'New Cloud Service', icon: 'Images/new-cloud.svg' }
    ]
}
```

### Adding New Sections

1. **Add HTML structure in `index.html`:**
```html
<section id="new-section" class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">New Section</h2>
            <p class="section-subtitle">Section description</p>
        </div>
        <div id="new-section-container">
            <!-- Content will be loaded dynamically -->
        </div>
    </div>
</section>
```

2. **Add navigation link:**
```html
<li><a href="#new-section" class="nav-link">New Section</a></li>
```

3. **Create content loader in `script.js`:**
```javascript
// In ContentLoader class
loadNewSection() {
    const container = document.getElementById('new-section-container');
    if (container) {
        container.innerHTML = this.createNewSectionContent();
    }
}

createNewSectionContent() {
    return `
        <div class="new-section-item">
            <!-- Your content here -->
        </div>
    `;
}
```

## 🎯 Customization Guide

### Changing Colors

The portfolio now includes 9 pre-designed color palettes. To customize:

1. **Use the palette selector** (🎨 button) to try different schemes
2. **Modify existing palettes** in `style.css` under the `[data-palette="..."]` sections
3. **Add new palettes** following the pattern shown above

### Changing Fonts

1. **Update Google Fonts link in `index.html`:**
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

2. **Update font family in `style.css`:**
```css
--font-family: 'YourFont', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Adding Animations

1. **Create new animation in `style.css`:**
```css
@keyframes yourAnimation {
    from { /* initial state */ }
    to { /* final state */ }
}

.your-animation-class {
    animation: yourAnimation 0.6s ease-out;
}
```

2. **Apply in `script.js` AnimationManager:**
```javascript
animateElement(element) {
    element.classList.add('your-animation-class');
}
```

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
