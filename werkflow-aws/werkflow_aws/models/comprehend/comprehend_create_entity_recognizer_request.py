from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_entity_recognizer_input_data_config import ComprehendEntityRecognizerInputDataConfig
from .comprehend_tag import ComprehendTag
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendCreateEntityRecognizerRequest(BaseModel):
    RecognizerName: StrictStr
    DataAccessRoleArn: StrictStr
    InputDataConfig: ComprehendEntityRecognizerInputDataConfig
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
    VersionName: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
    ClientRequestToken: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
    ModelKmsKeyId: StrictStr | None = None
    ModelPolicy: StrictStr | None = None
