from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointTemplateActiveVersionRequest(BaseModel):
    Version: StrictStr | None = None
