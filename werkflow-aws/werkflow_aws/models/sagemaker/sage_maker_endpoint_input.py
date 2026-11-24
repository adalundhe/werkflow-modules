from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerEndpointInput(BaseModel):
    EndpointName: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3InputMode: StrictStr | None = None
    S3DataDistributionType: StrictStr | None = None
    FeaturesAttribute: StrictStr | None = None
    InferenceAttribute: StrictStr | None = None
    ProbabilityAttribute: StrictStr | None = None
    ProbabilityThresholdAttribute: StrictFloat | StrictInt | None = None
    StartTimeOffset: StrictStr | None = None
    EndTimeOffset: StrictStr | None = None
    ExcludeFeaturesAttribute: StrictStr | None = None
