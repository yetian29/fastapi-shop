from fastapi import FastAPI


def init_app():
    app = FastAPI(debug=True, docs_url="/api/v1/docs")
    return app
