from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_output_data_config import ComprehendOutputDataConfig
from .comprehend_redaction_config import ComprehendRedactionConfig
from .comprehend_tag import ComprehendTag


class ComprehendStartPiiEntitiesDetectionJobRequest(BaseModel):
    InputDataConfig: ComprehendInputDataConfig
    OutputDataConfig: ComprehendOutputDataConfig
    Mode: Literal['ONLY_REDACTION', 'ONLY_OFFSETS']
    DataAccessRoleArn: StrictStr
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
    RedactionConfig: ComprehendRedactionConfig | None = None
    JobName: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
