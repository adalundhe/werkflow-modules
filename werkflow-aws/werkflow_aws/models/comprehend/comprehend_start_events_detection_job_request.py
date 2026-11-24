from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_output_data_config import ComprehendOutputDataConfig
from .comprehend_tag import ComprehendTag


class ComprehendStartEventsDetectionJobRequest(BaseModel):
    InputDataConfig: ComprehendInputDataConfig
    OutputDataConfig: ComprehendOutputDataConfig
    DataAccessRoleArn: StrictStr
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
    TargetEventTypes: list[StrictStr]
    JobName: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
