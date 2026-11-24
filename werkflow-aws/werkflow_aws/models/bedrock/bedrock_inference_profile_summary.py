from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_inference_profile_model import BedrockInferenceProfileModel


class BedrockInferenceProfileSummary(BaseModel):
    inferenceProfileName: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    inferenceProfileArn: StrictStr | None = None
    models: list[BedrockInferenceProfileModel] | None = None
    inferenceProfileId: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
