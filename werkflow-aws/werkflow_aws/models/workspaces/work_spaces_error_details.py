from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesErrorDetails(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
