[![ci](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml)

[![ci](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml)

[![ci](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/ci-cd-github-actions/actions/workflows/ci.yml)


# ci-cd-github-actions

Pipeline РЅР° GitHub Actions: lint в†’ tests в†’ build Docker image в†’ push РІ GHCR (GitHub Container Registry).

## РўРµС…РЅРѕР»РѕРіРёРё
- Python (Flask)
- Pytest, Ruff
- Docker / Docker Compose
- GitHub Actions
- GHCR (GitHub Container Registry)

## РљР°Рє Р·Р°РїСѓСЃС‚РёС‚СЊ (3 РєРѕРјР°РЅРґС‹)
```powershell
Copy-Item .env.example .env
docker compose up --build -d
curl.exe http://localhost:8000/health

