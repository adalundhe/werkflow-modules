from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_s3_data_config import PersonalizeS3DataConfig


class PersonalizeMetricAttributionOutput(BaseModel):
    s3DataDestination: PersonalizeS3DataConfig | None = None
    roleArn: StrictStr | None = None
