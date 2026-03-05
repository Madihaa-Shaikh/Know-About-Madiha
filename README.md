# Model Switch UI (Free Demo)

A lightweight, GitHub Pages–friendly UI that lets you switch between multiple “engines” (Helper / Dev / Guard) using a dropdown, then generate a demo response instantly.

## Features
- Dropdown-based routing (Engine selection)
- Tone selector (Simple / Professional / Roman Urdu)
- Guard mode (basic safety filter)
- Latency + metadata displayed
- No API keys, no backend required

## Architecture
UI (HTML/CSS)
  → Router (JS switch)
    → Engine Adapters (Helper / Dev / Guard)
      → Formatter (Tone)

## Run locally
Open `index.html` in your browser.

## Deploy on GitHub Pages
1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: `main`, Folder: `/root`
5. Save → Your site link will appear
