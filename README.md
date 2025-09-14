# JAL Monorepo

Backend: FastAPI + SQLAlchemy + PostgreSQL
Frontend: React + Vite
Infra: Azure Container Apps, Azure PostgreSQL Flexible Server, Azure Key Vault, App Insights

## Quickstart

### Backend

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
export POSTGRES_HOST=localhost POSTGRES_DB=jal POSTGRES_USER=jal POSTGRES_PASSWORD=jal
export SECRET_KEY=dev-secret ADMIN_EMAIL=admin@example.com ADMIN_PASSWORD=admin
uvicorn app.main:app --app-dir backend --reload
```

### Frontend

```bash
cd frontend && npm i && npm run dev
```

## Notes

- First run allows `ADMIN_PASSWORD` env if no `ADMIN_PASSWORD_HASH`.
- Replace `SECRET_KEY` in prod.