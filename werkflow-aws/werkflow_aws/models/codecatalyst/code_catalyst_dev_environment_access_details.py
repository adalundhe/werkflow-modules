from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDevEnvironmentAccessDetails(BaseModel):
    streamUrl: StrictStr | None = None
    tokenValue: StrictStr | None = None
