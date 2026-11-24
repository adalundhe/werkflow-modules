from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchNaturalLanguageQueryGenerationOptionsOutput(BaseModel):
    DesiredState: StrictStr | None = None
    CurrentState: StrictStr | None = None
