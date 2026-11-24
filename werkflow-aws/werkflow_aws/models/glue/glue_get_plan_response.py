from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetPlanResponse(BaseModel):
    PythonScript: StrictStr | None = None
    ScalaCode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
