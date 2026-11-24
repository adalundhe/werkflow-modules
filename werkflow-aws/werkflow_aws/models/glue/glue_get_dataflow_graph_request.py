from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataflowGraphRequest(BaseModel):
    PythonScript: StrictStr | None = None
