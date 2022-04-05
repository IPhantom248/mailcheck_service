from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.views import router


def get_application() -> FastAPI:
    app = FastAPI(title="mailcheck_service", debug=True)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )
    app.include_router(router)
    return app


app = get_application()
