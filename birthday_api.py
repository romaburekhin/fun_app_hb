from datetime import datetime


def create_app(html_path="index.html"):
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse, JSONResponse
    from pathlib import Path

    web_app = FastAPI()
    html = Path(html_path).read_text()

    @web_app.get("/")
    def ui():
        return HTMLResponse(html)

    @web_app.get("/api")
    def birthday():
        now = datetime.now()
        is_birthday = now.month == 12 and now.day == 27
        message = "happy birthday Roma" if is_birthday else "today is not your birthday, next time"
        return JSONResponse({"message": message})

    return web_app


if __name__ != "__main__":
    import modal

    image = (
        modal.Image.debian_slim()
        .pip_install("fastapi")
        .add_local_file("index.html", "/app/index.html")
    )
    app = modal.App("birthday-api", image=image)

    @app.function()
    @modal.asgi_app()
    def serve():
        return create_app("/app/index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
