from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AmplifyCreateDeploymentResponse(BaseModel):
    jobId: StrictStr | None = None
    fileUploadUrls: dict[StrictStr, StrictStr] | None = None
    zipUploadUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
