from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerInferenceRouterSummary(BaseModel):
    InferenceRouterName: StrictStr | None = None
    InferenceRouterArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
