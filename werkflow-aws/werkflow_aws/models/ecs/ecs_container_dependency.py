from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSContainerDependency(BaseModel):
    containerName: StrictStr | None = None
    condition: StrictStr | None = None
