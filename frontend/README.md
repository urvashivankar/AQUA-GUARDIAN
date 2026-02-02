# AQUA Guardian - Frontend UI

The user interface for the AQUA Guardian pollution monitoring system. Built with modern web technologies for a premium, fast, and responsive experience.

## Features

- 📱 **Responsive Dashboard**: Real-time analytics for water quality and pollution reports.
- 🤖 **AI Report Submission**: Seamless interface for uploading photos for instant AI classification.
- 🗺️ **Interactive Maps**: Geographic visualization of pollution hotspots and severity.
- 🏆 **Gamification**: Leaderboards and contribute rewards for active citizens.
- 🏛️ **Multi-Role Access**: Specialized dashboards for Citizens, NGOs, and Government authorities.

## Tech Stack

- **Framework**: React 18 with Vite
- **Language**: TypeScript
- **Styling**: Tailwind CSS & Framer Motion (animations)
- **UI Components**: shadcn/ui
- **State Management**: React Query (TanStack Query)
- **Auth & Database**: Supabase

## Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment Variables
Create a `.env.production` file for deployment or `.env.local` for development:
```env
VITE_API_URL=https://your-backend-api.com
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 3. Run Development Server
```bash
npm run dev
```

### 4. Build for Production
```bash
npm run build
```

## Production Readiness
The frontend has been sanitized for production:
- 🛡️ **No Hardcoded Links**: All API calls use environment variables.
- 🧹 **Cleanup**: All development-only tools and "setup-demo" routes have been removed.
- ⚡ **Optimized**: Ready for deployment on Vercel, Netlify, or Render.

---
Part of the AQUA Guardian Ecosystem.
