# 🚀 Vercel Deployment Guide

Complete step-by-step guide to deploy your beautiful birthday website to Vercel.

## What is Vercel?

Vercel is a free hosting platform perfect for static websites. Your site will be:
- **Free to host**: No hosting costs
- **Fast**: Served from global CDN
- **Secure**: HTTPS by default
- **Easy to update**: Just push changes

## Method 1: Using Vercel Dashboard (Easiest)

### Step 1: Prepare Your Files
1. Make sure all files are in the project folder:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `package.json`
   - `vercel.json`
   - `README.md`

### Step 2: Create GitHub Account (If you don't have one)
1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Complete the registration

### Step 3: Create GitHub Repository
1. Go to [github.com/new](https://github.com/new)
2. Repository name: `happy-birthday-sheena`
3. Description: `Interactive birthday greeting website for Sheena`
4. Choose "Public" (so it's easier to share)
5. Click "Create repository"

### Step 4: Upload Files to GitHub
Using GitHub Web Interface (No Git knowledge needed):

1. In your GitHub repository, click "Add file" → "Upload files"
2. Drag and drop your project files OR click to select them
3. Add a commit message: "Initial commit: Birthday website"
4. Click "Commit changes"

### Step 5: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "Sign up" or "Log in" (use your GitHub account)
3. Click "Create a Project"
4. Select "Import Git Repository"
5. Paste your GitHub repository URL
6. Click "Continue"
7. Project settings should auto-detect correctly
8. Click "Deploy"
9. Wait 30-60 seconds...
10. Click "Visit" to see your live site!

## Method 2: Using Vercel CLI (For Advanced Users)

### Prerequisites
- Node.js and npm installed

### Steps

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Open Terminal in Project Folder:**
```bash
cd "C:\Users\klim4\Desktop\Happy Birthday Sheena"
```

3. **Deploy:**
```bash
vercel
```

4. **Follow Prompts:**
   - Select "y" for "Set up and deploy?"
   - Select your scope/team
   - Confirm project name
   - Accept default settings
   - Wait for deployment

5. **Get Your URL:**
   - After success, you'll get a URL like: `https://happy-birthday-sheena.vercel.app`

## Method 3: Direct Upload (Fastest!)

1. Go to [vercel.com](https://vercel.com)
2. Don't have an account? Click "Sign up"
3. If asked, select "Hobby" (free plan)
4. Once logged in, look for "Drop here to import your project"
5. Drag your entire project folder onto the area
6. Wait for deployment
7. Your site is live!

## 🎯 After Deployment

### Get Your Live URL
- Vercel will give you a random URL like: `https://happy-birthday-sheena-xyz.vercel.app`
- You can customize it with a custom domain later

### Share Your Site
- Share the Vercel URL with Sheena and guests
- Works on all devices and browsers
- No installation needed - just open the link!

### Update Your Site

**If using GitHub method:**
1. Make changes to your files locally
2. Upload updated files to GitHub
3. Vercel automatically redeploys (within 1-2 minutes)

**If using CLI method:**
1. Make changes locally
2. Run `vercel` in terminal again
3. Confirm deployment

## 🌐 Custom Domain (Optional)

After deployment:
1. Go to your Vercel project dashboard
2. Settings → Domains
3. Add custom domain (e.g., `sheenabirthday.com`)
4. Follow DNS setup instructions
5. Takes 24-48 hours to activate

## 🔍 Troubleshooting

### Site Shows "404 Not Found"
- Make sure `index.html` is in the root directory
- Check that `vercel.json` has correct configuration

### Styling Looks Wrong
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Check that `styles.css` is in same folder as `index.html`

### JavaScript Not Working
- Check browser console for errors (F12)
- Make sure `script.js` is in same folder
- Verify file paths are correct

### Images Not Loading
- For placeholder images: They work automatically
- For custom images: Use full URL or upload to image hosting service
- Don't use local file paths in deployed version

## 📊 Monitor Your Site

Once deployed:
1. Visit your Vercel dashboard
2. View analytics and visitor data
3. Check performance metrics
4. Deploy new versions anytime

## 🎉 You're Done!

Your beautiful birthday website is now live! Share it with:
- Friends and family via the link
- Social media
- Email or messaging apps
- Print the QR code of the URL

---

**Need Help?**
- Vercel Support: [vercel.com/support](https://vercel.com/support)
- GitHub Help: [docs.github.com](https://docs.github.com)
- Common Issues: See troubleshooting section above

**Happy Deploying! 🚀**
