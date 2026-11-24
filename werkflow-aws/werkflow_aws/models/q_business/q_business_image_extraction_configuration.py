from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessImageExtractionConfiguration(BaseModel):
    imageExtractionStatus: StrictStr | None = None
