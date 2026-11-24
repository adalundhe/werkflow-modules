from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectExtractionDefinitionNotFoundBehavior(BaseModel):
    Behavior: StrictStr | None = None
    DefaultValue: StrictStr | None = None
