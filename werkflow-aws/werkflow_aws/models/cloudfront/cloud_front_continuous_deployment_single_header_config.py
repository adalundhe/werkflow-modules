from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontContinuousDeploymentSingleHeaderConfig(BaseModel):
    Header: StrictStr | None = None
    Value: StrictStr | None = None
