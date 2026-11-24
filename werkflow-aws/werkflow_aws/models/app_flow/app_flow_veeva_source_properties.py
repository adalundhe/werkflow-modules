from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowVeevaSourceProperties(BaseModel):
    object: StrictStr | None = None
    documentType: StrictStr | None = None
    includeSourceFiles: StrictBool | None = None
    includeRenditions: StrictBool | None = None
    includeAllVersions: StrictBool | None = None
