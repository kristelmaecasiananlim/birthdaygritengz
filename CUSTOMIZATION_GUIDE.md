# 🖼️ Image & Customization Guide

Quick guide to add your photos and customize the website.

## 🎨 Adding Images to the Gallery

### Where are the images?
They're in the `index.html` file under the **"Some Beautiful Memories"** section (around line 83-97).

### How to Add Your Photos

#### Option 1: Use Placeholder Images (Temporary)
The website currently uses placeholder images. They'll work fine temporarily:
- `https://via.placeholder.com/300x300/1e3a8a/ffffff?text=Memory+1`
- `https://via.placeholder.com/300x300/1e40af/ffffff?text=Memory+2`
- `https://via.placeholder.com/300x300/1e3a8a/ffffff?text=Memory+3`

#### Option 2: Upload to Free Image Hosting (Recommended)

**Use Imgur (Free, Easy):**
1. Go to [imgur.com](https://imgur.com)
2. Click "New Post"
3. Drag and drop your photos
4. Click "Post"
5. Right-click the image and copy the image URL
6. In `index.html`, replace the placeholder URL with your Imgur URL

**Alternative Free Services:**
- [Cloudinary](https://cloudinary.com) - Free with registration
- [Imgbb](https://imgbb.com) - No registration needed
- [Postimages](https://postimages.org) - Simple upload

#### Option 3: Host Images Locally (Advanced)
1. Place image files in the same folder as `index.html`
2. Change image path from `https://...` to just the filename
3. Example: `<img src="memory1.jpg" alt="Memory 1">`

## 🎯 The Gallery Section

Current code in `index.html`:
```html
<section class="gallery-section">
    <h2>Some Beautiful Memories 📸</h2>
    <div class="gallery">
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x300/1e3a8a/ffffff?text=Memory+1" alt="Memory 1">
            <p>Our first adventure</p>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x300/1e40af/ffffff?text=Memory+2" alt="Memory 2">
            <p>Unforgettable moments</p>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x300/1e3a8a/ffffff?text=Memory+3" alt="Memory 3">
            <p>Forever friends</p>
        </div>
    </div>
</section>
```

Replace with your image URLs and descriptions:
```html
<section class="gallery-section">
    <h2>Some Beautiful Memories 📸</h2>
    <div class="gallery">
        <div class="gallery-item">
            <img src="https://imgur.com/your-image-id.jpg" alt="Our first adventure">
            <p>Our first adventure</p>
        </div>
        <div class="gallery-item">
            <img src="https://imgur.com/second-image-id.jpg" alt="Fun times">
            <p>Unforgettable moments</p>
        </div>
        <div class="gallery-item">
            <img src="https://imgur.com/third-image-id.jpg" alt="Forever memories">
            <p>Forever friends</p>
        </div>
    </div>
</section>
```

## ✏️ Text Customization

### Change Names and Messages

**In the Header Section:**
```html
<h1 class="main-title">✨ Happy Birthday ✨</h1>
<p class="subtitle">Sheena Marie M. Caberte</p>
<p class="from-text">From your bestfriend, Kristel Mae C. Lim 💙</p>
```

**In the Message Section:**
```html
<p class="message-text">
    Happy Birthday to the most amazing friend! Thank you...
</p>
<p class="message-signature">With love and admiration,<br>Kristel Mae 💙</p>
```

### Change the "Why I Love You" Reasons

Find the section around line 127-149 and update the cards:
```html
<div class="reason-card" onclick="animateCard(this)">
    <span class="reason-emoji">😊</span>
    <p>Your smile is contagious</p>
</div>
```

Change emoji and text to your own reasons!

## 🌈 Change Colors

The website uses a blue theme. To change colors, edit `styles.css`:

```css
:root {
    --primary-blue: #1e3a8a;      /* Main dark blue */
    --secondary-blue: #1e40af;    /* Secondary blue */
    --light-blue: #3b82f6;        /* Bright blue */
    --lighter-blue: #93c5fd;      /* Light sky blue */
    --accent-blue: #0369a1;       /* Cyan blue */
    --white: #ffffff;
    --light-gray: #f3f4f6;
    --text-dark: #1f2937;
}
```

**Change to your favorite colors:**

**For Pink Theme:**
```css
:root {
    --primary-blue: #831843;      /* Dark pink */
    --secondary-blue: #be185d;    /* Pink */
    --light-blue: #ec4899;        /* Hot pink */
    --lighter-blue: #fbcfe8;      /* Light pink */
    --accent-blue: #db2777;       /* Bright pink */
    --white: #ffffff;
    --light-gray: #f3f4f6;
    --text-dark: #1f2937;
}
```

**For Purple Theme:**
```css
:root {
    --primary-blue: #4c1d95;      /* Dark purple */
    --secondary-blue: #6d28d9;    /* Purple */
    --light-blue: #a855f7;        /* Bright purple */
    --lighter-blue: #e9d5ff;      /* Light purple */
    --accent-blue: #9333ea;       /* Vibrant purple */
    --white: #ffffff;
    --light-gray: #f3f4f6;
    --text-dark: #1f2937;
}
```

**For Green Theme:**
```css
:root {
    --primary-blue: #134e4a;      /* Dark green */
    --secondary-blue: #065f46;    /* Forest green */
    --light-blue: #10b981;        /* Emerald green */
    --lighter-blue: #a7f3d0;      /* Light green */
    --accent-blue: #059669;       /* Bright green */
    --white: #ffffff;
    --light-gray: #f3f4f6;
    --text-dark: #1f2937;
}
```

Find your favorite colors at [htmlcolorcodes.com](https://htmlcolorcodes.com)

## 🎉 Change Emojis

You can replace any emoji with your favorites:
- Bouquet emojis: 🌹 💙 🌸 etc.
- Header emojis: ✨ 🎉 💙
- Section emojis: 📸 💌 💖 🌟

## 📱 Add More Photos

To add more than 3 photos, duplicate the gallery item:

```html
<div class="gallery-item">
    <img src="your-image-url.jpg" alt="Description">
    <p>Your description here</p>
</div>
```

Copy this whole block and paste it again in the gallery section.

## ❤️ Add More "Why I Love You" Cards

Copy this block and paste multiple times:

```html
<div class="reason-card" onclick="animateCard(this)">
    <span class="reason-emoji">🎉</span>
    <p>Your reason here</p>
</div>
```

Max recommended: 6-8 cards for best mobile display.

## 🔄 Apply Changes

After editing:

1. **Local Test**: Open `index.html` in your browser to see changes
2. **Push to GitHub**: Upload modified files
3. **Vercel Auto-Deploys**: Changes appear live within 1-2 minutes

## 🎁 Special Easter Egg Customization

The Konami code Easter egg message is in `script.js` around line 174:

```javascript
easterEgg.innerHTML = `
    <h2>🎉 EASTER EGG FOUND! 🎉</h2>
    <p>You've discovered a hidden message from Kristel! 💙</p>
    <p>"You're not just my best friend, you're my sister. Happy Birthday, Sheena!" 🌹</p>
`;
```

Customize this message to something more personal!

## 💡 Tips

- **Image Size**: Recommended 300x300px for gallery items
- **Image Quality**: Use JPG for photos, PNG for graphics
- **Load Time**: Smaller files (under 500KB) load faster
- **Mobile Test**: Always check how it looks on phone

## ❓ Common Issues

**Images show broken icon:**
- Check your image URL is correct
- Try a different image hosting service
- Make sure image file exists

**Message or text doesn't show:**
- Check quotation marks are correct
- Don't use special characters that need escaping
- Test in incognito mode (clear cache)

**Colors look different than expected:**
- Check color code is valid hex format
- Clear browser cache and reload
- Try the exact color codes from color picker

---

**Any Questions?**
Check the main README.md for more help!

**Enjoy customizing your beautiful birthday website! 🎉**
