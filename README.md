# Newcastle: The Northern Powerhouse

Welcome to the **Newcastle: The Northern Powerhouse** project! This is a comprehensive, multi-page, fully responsive website designed to showcase Newcastle as a leading city in the UK’s Northern Powerhouse initiative. The site highlights Newcastle’s history, demography, investment climate, and unique opportunities for growth and investment, and provides a modern, accessible, and visually engaging user experience.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Responsive Design & Accessibility](#responsive-design--accessibility)
- [Screenshots](#screenshots)
- [Testing & Validation](#testing--validation)
- [Performance](#performance)
- [How to Use](#how-to-use)
- [Deployment](#deployment)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This project is a showcase website for Newcastle, UK, as part of the Northern Powerhouse initiative. It is intended for investors, students, and the general public interested in the city’s economic, cultural, and social strengths. The site is built with modern web standards and best practices, ensuring accessibility, responsiveness, and a seamless user experience across all devices.

---

## Features

- **Fully Responsive Design:** Optimized for desktop, tablet, and mobile devices.
- **Bootstrap Carousel:** Used on multiple pages for interactive content display.
- **Custom Cards & Lists:** For clear, scannable presentation of key information.
- **Accessible Navigation:** Semantic HTML and ARIA labels for improved accessibility.
- **Contact Page:** Includes address, Google Maps embed, and a functional contact form.
- **Consistent Footer:** Social media links and copyright.
- **Optimized Images:** Use of JPEG and WebP for performance.
- **Modern UI:** Gold and dark color scheme for a professional look.
- **JavaScript Interactivity:** Bootstrap JS for carousel and navbar toggling.
- **Testing Evidence:** HTML, CSS, and performance validation included.
- **Screenshots:** Desktop and mobile screenshots for all pages.
- **Performance Optimized:** Fast load times and efficient resource usage.
- **Accessible Forms:** All form fields have labels and proper contrast.
- **Keyboard Navigation:** Navbar and carousel controls are keyboard accessible.
- **Alt Text:** All images include descriptive alt attributes.
- **Consistent Spacing:** Padding and margins ensure content is never clipped or hidden, regardless of device.

---

## Technologies Used

- **HTML5** – Semantic markup for structure and accessibility.
- **CSS3** – Custom styles and responsive utilities in [`assets/css/style.css`](assets/css/style.css).
- **Bootstrap 5** – Layout, grid, navbar, carousel, and responsive utilities.
- **Bootstrap Icons** – For social and UI icons.
- **Google Fonts** – For custom typography.
- **JavaScript** – Bootstrap’s JS bundle for carousel and navbar interactivity.
- **Google Maps Embed** – For the contact page.
- **WebP/JPEG Images** – For fast loading and high quality.

---

## Project Structure

```markdown
## Project Structure

```
/
├── index.html
├── history.html
├── demography.html
├── investment-climate.html
├── opportunities.html
├── contact.html
├── success.html
├── README.md
└── assets/
    ├── css/
    │   └── style.css
    └── images/
        ├── home.jpg
        ├── history.webp
        ├── demography.webp
        ├── investment.jpg
        ├── dalmatian.jpg
        ├── NNPHhomedesktop.png
        ├── NNPHhomemobile.png
        ├── NNPHhistorydesktop.png
        ├── NNPHhistorymobile.png
        ├── NNPHdemographydesktop.png
        ├── NNPHdemographymobile.png
        ├── NNPHinvestmentdesktop.png
        ├── NNPHinvestmentmobile.png
        ├── NNPHopportunitiesdesktop.png
        ├── NNPHopportunitiesmobile.png
        ├── contact.png
        ├── NNPHcontactmobile.png
        ├── NNPHsuccessdesktop.png
        ├── NNPHsuccessmobile.png
        ├── NNPHw3chtmlvalidation.png
        ├── NNPHw3ccssvalidation.png
        ├── NNPHlighthousemobile.png
        └── NNPHlighthousedesktop.png
```

---

---
``` 
## Responsive Design & Accessibility

- **Mobile-First:** The layout and all components are designed to adapt seamlessly to all screen sizes, from large desktops to small mobile devices.
- **Accessible Forms:** All form fields include visible labels and sufficient color contrast for readability.
- **Keyboard Navigation:** The navbar, carousel, and all interactive elements are accessible via keyboard.
- **Alt Text:** All images include descriptive `alt` attributes for screen readers.
- **Consistent Spacing:** Padding and margins ensure content is never clipped or hidden, regardless of device or orientation.
- **Footer:** The footer is fixed to the bottom of the page and never overlaps content.
- **Background Images:** Section backgrounds always cover their containers fully, maintaining visual integrity on all devices.

---

## Screenshots

### Home Page Desktop
<img src="assets/images/NNPHhomedesktop.png" alt="Home Page Desktop view" width="100%">

### Home Page Mobile
<img src="assets/images/NNPHhomemobile.png" alt="Home Page Mobile View" width="300">

### History Page Desktop
<img src="assets/images/NNPHhistorydesktop.png" alt="History Page Desktop View" width="100%">

### History Page Mobile
<img src="assets/images/NNPHhistorymobile.png" alt="History Page Mobile View" width="300">

### Demography Page Desktop
<img src="assets/images/NNPHdemographydesktop.png" alt="Demography Page Desktop View" width="100%">

### Demography Page Mobile
<img src="assets/images/NNPHdemographymobile.png" alt="Demography Page Mobile View" width="300">

### Investment-Climate Page Desktop
<img src="assets/images/NNPHinvestmentdesktop.png" alt="Investment-Climate Page Desktop View" width="100%">

### Investment-Climate Page Mobile
<img src="assets/images/NNPHinvestmentmobile.png" alt="Investment-Climate Page Mobile View" width="300">

### Opportunities Page Desktop
<img src="assets/images/NNPHopportunitiesdesktop.png" alt="Opportunities Page Desktop View" width="100%">

### Opportunities Page Mobile
<img src="assets/images/NNPHopportunitiesmobile.png" alt="Opportunities Page Mobile View" width="300">

### Contact Page Desktop
<img src="assets/images/contact.png" alt="Contact Page Desktop View" width="100%">

### Contact Page Mobile
<img src="assets/images/NNPHcontactmobile.png" alt="Contact Page Mobile View" width="300">

### Success Page Desktop
<img src="assets/images/NNPHsuccessdesktop.png" alt="Success Page Desktop View" width="100%">


---

## Testing & Validation

### HTML Validation

<img src="assets/images/NNPHw3chtmlvalidation.png" alt="HTML Validation" width="100%">

### CSS Validation

<img src="assets/images/NNPHw3ccssvalidation.png" alt="CSS Validation" width="100%">

### Lighthouse Performance (Mobile)

<img src="assets/images/NNPHlighthousemobile.png" alt="Lighthouse Performance Mobile" width="300">

### Lighthouse Performance (Desktop)

<img src="assets/images/NNPHlighthousedesktop.png" alt="Lighthouse Performance Desktop" width="100%">

### Manual Testing

- All navigation links work and highlight the current page.
- Carousels are swipeable and keyboard accessible.
- Contact form validates required fields and displays labels on all screen sizes.
- Footer remains at the bottom and is never overlapped by content.
- Background images cover their sections fully on all devices.
- All content is readable and accessible on mobile, tablet, and desktop.

---

## Performance

- Images are optimized (WebP/JPEG).
- CSS is consolidated and commented for maintainability.
- Carousels and navigation are fully accessible and responsive.
- Lighthouse scores are high for performance, accessibility, and best practices.

---

## How to Use

1. **Clone or Download** this repository.
2. Open `index.html` in your browser.
3. Navigate using the navbar to explore all pages.
4. Use the contact form to send a message (demo only; no backend).
5. For best results, use a modern browser (Bootstrap 5 required for full interactivity).

---

## Deployment

To deploy this project:

1. Upload all files and folders to your web server or hosting platform.
2. Ensure the directory structure is preserved.
3. Open `index.html` in your browser to verify the site loads correctly.
4. All links and images should work out of the box; no build step is required.

---

## Known Issues

- The contact form is for demonstration only and does not send emails.
- Some images are placeholders and may be replaced with higher-resolution or licensed images as needed.
- If you encounter any issues with responsiveness or accessibility, please open an issue or contact the author.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. For major changes, please open an issue first to discuss what you would like to change.

---

## Credits

- [Bootstrap 5](https://getbootstrap.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [Unsplash](https://unsplash.com/) (for placeholder images)
- [Font Awesome](https://fontawesome.com/) (if used)
- Newcastle City Council (for address reference)
- Code Institute
- Full Stack AI-Augmented Developer Course Faculty and Students @waes.ac.uk
- Munawar Nadeem – Course Tutor
- All contributors and testers

---

## License

**Copyright © 2025 Mobolaji Onafuwa**

For commercial use or redistribution, please contact the author.

---