from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_attribute import ECSAttribute


class ECSDeleteAttributesRequest(BaseModel):
    attributes: list[ECSAttribute]
    cluster: StrictStr | None = None
