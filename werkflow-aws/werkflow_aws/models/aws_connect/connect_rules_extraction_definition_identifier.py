from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRulesExtractionDefinitionIdentifier(BaseModel):
    Identifier: StrictStr | None = None
