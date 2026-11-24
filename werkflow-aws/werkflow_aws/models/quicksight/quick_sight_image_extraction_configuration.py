from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightImageExtractionConfiguration(BaseModel):
    imageExtractionStatus: StrictStr | None = None
