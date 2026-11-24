from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_recommendation_job_payload_config import SageMakerRecommendationJobPayloadConfig


class SageMakerRecommendationJobContainerConfig(BaseModel):
    Domain: StrictStr | None = None
    Task: StrictStr | None = None
    Framework: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
    PayloadConfig: SageMakerRecommendationJobPayloadConfig | None = None
    NearestModelName: StrictStr | None = None
    SupportedInstanceTypes: list[StrictStr] | None = None
    SupportedEndpointType: StrictStr | None = None
    DataInputConfig: StrictStr | None = None
    SupportedResponseMIMETypes: list[StrictStr] | None = None
