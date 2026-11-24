from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AmplifyStartDeploymentRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobId: StrictStr | None = None
    sourceUrl: StrictStr | None = None
    sourceUrlType: Literal['ZIP', 'BUCKET_PREFIX'] | None = None
