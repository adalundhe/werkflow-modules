from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMStartSessionRequest(BaseModel):
    Target: StrictStr
    DocumentName: StrictStr | None = None
    Reason: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
