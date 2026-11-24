from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class HealthImagingDeleteImageSetResponse(BaseModel):
    datastoreId: StrictStr | None = None
    imageSetId: StrictStr | None = None
    imageSetState: StrictStr | None = None
    imageSetWorkflowStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
