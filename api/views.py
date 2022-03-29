from typing import Any, Dict, List

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic.main import BaseModel
from decouple import config

# from api import schemas
# from api.models import Model1, Model2, Model3

async def get_token_header(x_token: str = Header(...)):
    if x_token != config("AUTH_TOKEN"):
        raise HTTPException(status_code=400, detail="X-Token header invalid")


router = APIRouter(
    prefix="/api/v1",
    tags=["views"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# CRUD
# Получение списка сущностей
# @router.get("/models", response_model=List[schemas.Model1])
# def read_models():
#     return list(Model1.objects.all())


# Создание сущности
# @router.post("/models", response_model=schemas.Model1)
# def create_model(model1: schemas.Model1):
#     return Model1.objects.create(**model1.dict(exclude_unset=True))


# Удаление сущности
# @router.delete("/models/{model1_id}")
# def delete_model(model1_id: int):
#     deleted_count = Model1.objects.filter(id=model1_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"Model1 {model1_id} not found")


# Получение списка сущностей, со связями
# @router.get("/get_realted_objects", response_model=List[schemas.Model2])
# def get_related_objects(user_id: int):
#     return schemas.Model2.from_qs(
#         instances=Model2.objects.filter(user_id=user_id),
#         relation_fields=[
#             schemas.RelationFields(
#                 field="many_related_models", serializer=schemas.Model3
#             )
#         ],
#     )


# Реквест с использованием body
# class PostBodyRequest(BaseModel):
#     title: str
#     struct: Any

# @router.post("/post_request_with_body")
# def post_request_with_body(body: PostBodyRequest):
#     ... use body