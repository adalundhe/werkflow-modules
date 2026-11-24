from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSuppressionListDestination(BaseModel):
    SuppressionListImportAction: StrictStr | None = None
