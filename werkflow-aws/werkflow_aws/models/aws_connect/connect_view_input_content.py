from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectViewInputContent(BaseModel):
    Template: StrictStr | None = None
    Actions: list[StrictStr] | None = None
