from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateContextRequest(BaseModel):
    ContextName: StrictStr
    Description: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    PropertiesToRemove: list[StrictStr] | None = None
