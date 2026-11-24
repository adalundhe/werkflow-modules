from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_failed_entity import KendraFailedEntity


class KendraAssociateEntitiesToExperienceResponse(BaseModel):
    FailedEntityList: list[KendraFailedEntity] | None = None
    ResponseMetadata: dict[str, Any] | None = None
