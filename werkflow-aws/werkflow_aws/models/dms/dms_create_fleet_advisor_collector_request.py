from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSCreateFleetAdvisorCollectorRequest(BaseModel):
    CollectorName: StrictStr
    ServiceAccessRoleArn: StrictStr
    S3BucketName: StrictStr
    Description: StrictStr | None = None
