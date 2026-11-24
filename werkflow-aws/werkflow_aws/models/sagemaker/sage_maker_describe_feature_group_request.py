from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeFeatureGroupRequest(BaseModel):
    FeatureGroupName: StrictStr
    NextToken: StrictStr | None = None
