from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_tag import ECSTag


class ECSEBSTagSpecification(BaseModel):
    resourceType: StrictStr | None = None
    tags: list[ECSTag] | None = None
    propagateTags: StrictStr | None = None
