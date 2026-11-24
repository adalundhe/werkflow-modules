from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerInferenceComponentSummary(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    InferenceComponentArn: StrictStr | None = None
    InferenceComponentName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    EndpointName: StrictStr | None = None
    VariantName: StrictStr | None = None
    InferenceComponentStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
