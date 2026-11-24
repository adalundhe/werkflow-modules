from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSCreateFleetAdvisorCollectorResponse(BaseModel):
    CollectorReferencedId: StrictStr | None = None
    CollectorName: StrictStr | None = None
    Description: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
