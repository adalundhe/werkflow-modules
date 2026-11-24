from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKFindingRemediation(BaseModel):
    Action: StrictStr | None = None
    DocumentationUrl: StrictStr | None = None
