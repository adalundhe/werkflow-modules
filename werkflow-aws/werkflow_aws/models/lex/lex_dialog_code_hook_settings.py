from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexDialogCodeHookSettings(BaseModel):
    enabled: StrictBool | None = None
