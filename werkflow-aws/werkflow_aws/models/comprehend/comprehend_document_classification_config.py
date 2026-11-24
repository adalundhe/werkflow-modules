from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDocumentClassificationConfig(BaseModel):
    Mode: StrictStr | None = None
    Labels: list[StrictStr] | None = None
