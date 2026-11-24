from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectViewContent(BaseModel):
    InputSchema: StrictStr | None = None
    Template: StrictStr | None = None
    Actions: list[StrictStr] | None = None
