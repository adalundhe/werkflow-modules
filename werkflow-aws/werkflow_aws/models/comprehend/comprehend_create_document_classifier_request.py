from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_document_classifier_input_data_config import ComprehendDocumentClassifierInputDataConfig
from .comprehend_document_classifier_output_data_config import ComprehendDocumentClassifierOutputDataConfig
from .comprehend_tag import ComprehendTag
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendCreateDocumentClassifierRequest(BaseModel):
    DocumentClassifierName: StrictStr
    DataAccessRoleArn: StrictStr
    InputDataConfig: ComprehendDocumentClassifierInputDataConfig
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
    VersionName: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
    OutputDataConfig: ComprehendDocumentClassifierOutputDataConfig | None = None
    ClientRequestToken: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
    Mode: Literal['MULTI_CLASS', 'MULTI_LABEL'] | None = None
    ModelKmsKeyId: StrictStr | None = None
    ModelPolicy: StrictStr | None = None
