from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetConnectionRequest(BaseModel):
    Name: StrictStr
    CatalogId: StrictStr | None = None
    HidePassword: StrictBool | None = None
    ApplyOverrideForComputeEnvironment: Literal['SPARK', 'ATHENA', 'PYTHON'] | None = None
