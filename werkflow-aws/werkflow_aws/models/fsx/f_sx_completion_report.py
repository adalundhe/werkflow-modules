from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FSxCompletionReport(BaseModel):
    Enabled: StrictBool | None = None
    Path: StrictStr | None = None
    Format: StrictStr | None = None
    Scope: StrictStr | None = None
