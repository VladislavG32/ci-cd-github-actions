[![ci](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml)

# ci-cd-github-actions

Pipeline на GitHub Actions: lint → tests → build Docker image → push в GHCR (GitHub Container Registry).

## Технологии
- Python (Flask)
- Ruff, Pytest
- Docker / Docker Compose
- GitHub Actions
- GHCR

## Как запустить (3 команды)
```powershell
Copy-Item .env.example .env
docker compose up --build -d
curl.exe http://localhost:8000/health
