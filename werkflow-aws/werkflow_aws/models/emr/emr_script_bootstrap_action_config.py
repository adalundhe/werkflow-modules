from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRScriptBootstrapActionConfig(BaseModel):
    Path: StrictStr | None = None
    Args: list[StrictStr] | None = None
