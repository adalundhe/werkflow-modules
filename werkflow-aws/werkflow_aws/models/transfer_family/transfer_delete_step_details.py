from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteStepDetails(BaseModel):
    Name: StrictStr | None = None
    SourceFileLocation: StrictStr | None = None
