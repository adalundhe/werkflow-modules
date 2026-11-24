from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectExtractionDefinitionDisplay(BaseModel):
    Label: StrictStr | None = None
