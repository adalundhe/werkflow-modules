from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_entity import ComprehendEntity


class ComprehendBatchDetectEntitiesItemResult(BaseModel):
    Index: StrictInt | None = None
    Entities: list[ComprehendEntity] | None = None
