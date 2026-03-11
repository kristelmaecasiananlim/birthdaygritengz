# 🎉 Happy Birthday Sheena - Interactive Greeting Website

A beautiful, interactive blue-themed bouquet greeting website created with love for **Sheena Marie M. Caberte** from **Kristel Mae C. Lim**.

## ✨ Features

### Interactive Elements
- **Animated Bouquet**: Floating, animated flowers that react to hover interactions
- **Surprise Modal**: Click the surprise button for a delightful reveal with confetti animation
- **Confetti Celebration**: Cascade of colorful confetti with emoji effects
- **"Why I Love You" Cards**: Interactive reason cards that flip and glow when clicked
- **Wish Stars**: Click stars to reveal personalized wish messages
- **Parallax Scrolling**: Smooth scroll effects for enhanced visual experience
- **Easter Egg**: Type the Konami code (↑↑↓↓←→←→BA) for a hidden message!

### Visual Design
- **Blue Color Scheme**: Elegant gradient background with multiple shades of blue
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Smooth Animations**: All elements feature polished animations and transitions
- **Modern Typography**: Clean, readable fonts with proper hierarchy
- **Glass-morphism Effects**: Frosted glass effects on cards and sections

### Sections
1. **Header**: Personalized greeting with names
2. **Bouquet Display**: Interactive animated bouquet with celebration button
3. **Photo Gallery**: For adding memories with Sheena
4. **Heartfelt Message**: A special message from Kristel to Sheena
5. **Why I Love You**: Six interactive reason cards showing appreciation
6. **Make a Wish**: Interactive star section for special wishes
7. **Final Celebration**: Grand finale with confetti button

## 🚀 Getting Started

### Local Development

1. Clone or download this project
2. Open `index.html` in your web browser
3. Alternatively, run a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (http-server)
npx http-server -p 3000
```

Then open `http://localhost:8000` (or 3000 if using http-server) in your browser.

## 📸 Adding Your Photos

The website uses placeholder images from `https://via.placeholder.com/`. To add your own photos:

1. Open `index.html` in a text editor
2. Find the gallery section (around line 83-97)
3. Replace the placeholder image URLs with your actual image URLs:

```html
<!-- Original -->
<img src="https://via.placeholder.com/300x300/1e3a8a/ffffff?text=Memory+1" alt="Memory 1">

<!-- Changed to your image -->
<img src="path/to/your/image1.jpg" alt="Memory 1">
```

### Upload Images:
- **Local**: Place images in the project folder and use relative paths
- **Cloud**: Upload to Imgur, Cloudinary, or another image hosting service and use the URLs

Example with cloud hosting:
```html
<img src="https://imgur.com/your-image-id.jpg" alt="Memory 1">
```

## 🌐 Deploying to Vercel

### Option 1: Using Vercel CLI

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Navigate to project directory:
```bash
cd "path/to/Happy Birthday Sheena"
```

3. Deploy:
```bash
vercel
```

4. Follow the prompts and your site will be live!

### Option 2: GitHub Integration

1. Push your project to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Select the project folder
6. Click "Deploy"

### Option 3: Drag & Drop

1. Go to [vercel.com](https://vercel.com)
2. Drag and drop your project folder
3. Wait for deployment to complete

## 🎨 Customization

### Change Colors
Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-blue: #1e3a8a;
    --secondary-blue: #1e40af;
    --light-blue: #3b82f6;
    /* ... adjust colors as needed */
}
```

### Change Text
Edit the HTML in `index.html`:
- Names, messages, and reason cards can all be customized
- Update emoji selections to match your preference
- Modify the special message in the message section

### Add/Remove Sections
- Copy section HTML and paste to add new sections
- Delete any section you don't need
- All sections have unique styling for consistent design

## 🔧 Technical Details

- **Pure HTML/CSS/JavaScript**: No dependencies required
- **Responsive Design**: Mobile-first approach with media queries
- **Web Audio API**: Sound effects for celebrations
- **CSS Animations**: Smooth, performance-optimized animations
- **Modern JavaScript**: ES6+ features with good browser support
- **Vercel Compatible**: Optimized for static site hosting

## 📁 Project Structure

```
Happy Birthday Sheena/
├── index.html          # Main HTML file
├── styles.css          # All styling and animations
├── script.js           # Interactive functionality
├── package.json        # Project metadata
├── vercel.json         # Vercel configuration
└── README.md          # This file
```

## 🎯 Features You Can Explore

1. **Click the "Surprise!" button**: Watch the confetti celebrate
2. **Hover over flowers**: They'll dance and respond
3. **Click reason cards**: They flip with animations
4. **Click stars**: Get personalized wishes
5. **Scroll down**: Enjoy parallax effects
6. **Type Konami code** (↑↑↓↓←→←→BA): Unlock the Easter egg!

## 💡 Tips for the Best Experience

- Test on different devices (phone, tablet, desktop)
- Replace placeholder images with real memories
- Customize the color scheme to Sheena's favorite colors
- Add more reason cards if desired
- Update the special message with personal touches
- Share the deployed link with everyone who wants to celebrate!

## 🔐 Privacy & Sharing

- This is a static website with no backend or database
- No personal data is collected or stored
- Safe to share publicly and with all guests
- Each view is completely independent

## 🎁 Future Enhancement Ideas

- Add a photo upload feature
- Include a music player with birthday songs
- Add a guestbook for messages
- Create a countdown timer
- Add video message support
- Include a playlist of special songs

## 📝 License

This project is created with love. Feel free to use and customize for your celebrations!

---

**Created with 💙 by Kristel Mae C. Lim for Sheena Marie M. Caberte**

**Happy Birthday, Sheena! 🎉🎂✨**
