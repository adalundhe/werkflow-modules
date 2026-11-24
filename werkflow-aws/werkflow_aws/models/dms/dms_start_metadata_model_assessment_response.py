from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSStartMetadataModelAssessmentResponse(BaseModel):
    RequestIdentifier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
