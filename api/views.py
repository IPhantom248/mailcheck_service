import aioredis
from decouple import config
from fastapi import APIRouter

BROKER_URL = config("BROKER_URL", default="redis://localhost:6379")

router = APIRouter(
    prefix="/api/v1",
    tags=["views"],
    responses={404: {"description": "Not found"}},
)


@router.get("/check_mail/")
async def check_mail(email: str):
    redis = await aioredis.from_url(BROKER_URL)
    domain = email.split("@")[1]

    if await redis.sismember("disposable_domains", domain):
        return {
            "domain": domain,
            "disposable": True,
            "public": False,
            "corporate": False,
        }
    if await redis.sismember("public_domains", domain):
        return {
            "domain": domain,
            "disposable": False,
            "public": True,
            "corporate": False,
        }
    return {"domain": domain, "disposable": False, "public": False, "corporate": True}
