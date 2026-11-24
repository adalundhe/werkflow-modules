from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchAutoTuneOptionsOutput(BaseModel):
    State: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    UseOffPeakWindow: StrictBool | None = None
