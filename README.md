# Birthday API

A simple API + UI that checks if today is Roma's birthday (December 27th).

**Live:** https://romaburekhin--birthday-api-serve.modal.run

## Endpoints

| Route | Description |
|-------|-------------|
| `GET /` | Web UI |
| `GET /api` | JSON response |

## Structure

```
├── birthday_api.py   # Modal app (routes + logic)
├── index.html        # UI template
├── requirements.txt
└── .gitignore
```

## Run Locally

```bash
pip3 install fastapi uvicorn
python3 birthday_api.py
```

Open http://localhost:8000 in your browser.

## Deploy

```bash
pip3 install modal
python3 -m modal setup   # authenticate once
modal deploy birthday_api.py
```
