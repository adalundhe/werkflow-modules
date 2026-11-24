from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsInputLambdaProcessorDescription(BaseModel):
    ResourceARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
