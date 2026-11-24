from __future__ import annotations
from pydantic import BaseModel
from .personalize_s3_data_config import PersonalizeS3DataConfig


class PersonalizeBatchInferenceJobInput(BaseModel):
    s3DataSource: PersonalizeS3DataConfig | None = None
