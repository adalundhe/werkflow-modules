from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystProjectInformation(BaseModel):
    name: StrictStr | None = None
    projectId: StrictStr | None = None
