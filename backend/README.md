# AQUA Guardian - Backend API

FastAPI backend server for the AQUA Guardian pollution reporting and monitoring system.

## Features

- 🔐 User authentication with Supabase
- 📊 Real-time dashboard analytics
- 🤖 AI-powered pollution image classification
- 🗺️ Geographic pollution tracking
- ⛓️ Blockchain integration for report verification
- 📧 Automated authority notifications

## Prerequisites

- Python 3.9 or higher
- Virtual environment (venv)
- Supabase account and credentials

## Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the backend directory with the following:

```env
ENVIRONMENT=production
ALLOWED_ORIGINS=https://your-frontend-domain.com
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_SECRET_KEY=your_supabase_service_role_key
GROQ_API_KEY=your_groq_api_key
```

## Running the Server

### Manual Start

**Windows:**
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

**Linux/Mac:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`

## API Documentation

Access the interactive API documentation at:

- **Swagger UI**: http://localhost:8000/docs (Note: Disabled when `ENVIRONMENT=production`)
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
backend/
├── api/              # API route handlers
│   ├── auth.py       # Authentication & Security
│   ├── reports.py    # Pollution reporting logic
│   ├── dashboard.py  # Analytics & Statistics
│   └── ...           # Rewards, Cleanup, Notifications
├── db/               # Database migrations and Supabase client
├── ml/               # AI inference (Groq Vision)
├── blockchain/       # Web3 & Smart Contract integration
├── middleware/       # Security, Logging & Rate limiting
├── utils/            # Shared utility functions
└── main.py           # FastAPI entry point
```

## Initialization Scripts

For first-time setup, use these essential scripts in order:
1. `python scripts/run_migrations.py`: Prepare database schema.
2. `python scripts/admin_setup.py`: Initialize admin configurations.
3. `python scripts/seed_jurisdictions.py`: Setup geographic routing.
4. `python scripts/apply_rls.py`: Enable security policies.

### Database Connection Issues

Verify your Supabase credentials in the `.env` file and ensure your Supabase project is active.

## Development

### Adding New Endpoints

1. Create or modify files in the `api/` directory
2. Import and register the router in `main.py`
3. The server will auto-reload with `--reload` flag

### Running Tests

```bash
pytest tests/
```

## License

Part of the AQUA Guardian project.
