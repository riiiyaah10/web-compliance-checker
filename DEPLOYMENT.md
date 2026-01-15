# Deployment Instructions for Render

## Prerequisites
1. GitHub account
2. Render account (free at https://render.com)

## Steps to Deploy

### 1. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit - Web Compliance Checker"
```

### 2. Push to GitHub
```bash
# Create a new repository on GitHub (https://github.com/new)
# Then push your code:

git remote add origin https://github.com/YOUR_USERNAME/web-compliance-checker.git
git branch -M main
git push -u origin main
```

### 3. Deploy on Render
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in the details:
   - **Name**: web-compliance-checker
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free (default)

5. Click "Create Web Service"

### 4. Access Your App
Your app will be live at: `https://web-compliance-checker.onrender.com`

## Features
- ✅ Free hosting
- ✅ Auto-deploys from GitHub (push to update)
- ✅ HTTPS included
- ✅ Custom domain support (optional)

## Important Notes
- Free tier has limitations (spins down after 15 minutes of inactivity)
- For production, consider upgrading to a paid plan
- Keep your GitHub repo public for easier deployment

## Environment Variables (Optional)
If you need to add environment variables:
1. In Render dashboard → Environment
2. Add your custom variables

## Troubleshooting
- Check Render logs: Dashboard → Logs tab
- Ensure all dependencies are in `requirements.txt`
- Make sure `Procfile` is in the root directory
