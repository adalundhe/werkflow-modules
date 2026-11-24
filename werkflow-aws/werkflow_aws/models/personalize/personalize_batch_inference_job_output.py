from __future__ import annotations
from pydantic import BaseModel
from .personalize_s3_data_config import PersonalizeS3DataConfig


class PersonalizeBatchInferenceJobOutput(BaseModel):
    s3DataDestination: PersonalizeS3DataConfig | None = None
