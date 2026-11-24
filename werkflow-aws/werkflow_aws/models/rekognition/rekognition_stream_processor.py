from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionStreamProcessor(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
