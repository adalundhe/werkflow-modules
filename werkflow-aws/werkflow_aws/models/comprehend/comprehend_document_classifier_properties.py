from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_classifier_metadata import ComprehendClassifierMetadata
from .comprehend_document_classifier_input_data_config import ComprehendDocumentClassifierInputDataConfig
from .comprehend_document_classifier_output_data_config import ComprehendDocumentClassifierOutputDataConfig
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendDocumentClassifierProperties(BaseModel):
    DocumentClassifierArn: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    SubmitTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    TrainingStartTime: datetime.datetime | StrictStr | None = None
    TrainingEndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: ComprehendDocumentClassifierInputDataConfig | None = None
    OutputDataConfig: ComprehendDocumentClassifierOutputDataConfig | None = None
    ClassifierMetadata: ComprehendClassifierMetadata | None = None
    DataAccessRoleArn: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
    Mode: StrictStr | None = None
    ModelKmsKeyId: StrictStr | None = None
    VersionName: StrictStr | None = None
    SourceModelArn: StrictStr | None = None
    FlywheelArn: StrictStr | None = None
