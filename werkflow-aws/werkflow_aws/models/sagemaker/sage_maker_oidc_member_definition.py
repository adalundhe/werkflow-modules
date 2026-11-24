from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOidcMemberDefinition(BaseModel):
    Groups: list[StrictStr] | None = None
