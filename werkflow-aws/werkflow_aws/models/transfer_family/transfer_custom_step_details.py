from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferCustomStepDetails(BaseModel):
    Name: StrictStr | None = None
    Target: StrictStr | None = None
    TimeoutSeconds: StrictInt | None = None
    SourceFileLocation: StrictStr | None = None
