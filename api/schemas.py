from typing import List, Optional, Dict
from django.db import models

from pydantic import BaseModel as _BaseModel
from pydantic.types import Any


class RelationFields(_BaseModel):
    field: str
    serializer: Any = ...


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]

    @classmethod
    def from_qs(
        cls, instances: List[models.Model], relation_fields: List[RelationFields] = []
    ):
        data = []
        for _inst in instances:
            inst = cls.from_orm(_inst)

            for f in relation_fields:
                relations = getattr(inst, f.field)
                setattr(inst, f.field, f.serializer.from_orms(relations.all()))

            data.append(inst)

        return data


# class Model1(BaseModel):
#     id: Optional[int]
#     title: str

#     class Config:
#         orm_mode = True

# class Model2(BaseModel):
#     id: int
#     title: str
#     model1_id: int
#     model1: Model1
#     many_related_models: Any

#     class Config:
#         orm_mode = True

# class ManyRelatedModel(BaseModel):
#     model2_id: int
#     title: str

#     class Config:
#         orm_mode = True