from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_entity_recognizer_input_data_config import ComprehendEntityRecognizerInputDataConfig
from .comprehend_entity_recognizer_metadata import ComprehendEntityRecognizerMetadata
from .comprehend_entity_recognizer_output_data_config import ComprehendEntityRecognizerOutputDataConfig
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendEntityRecognizerProperties(BaseModel):
    EntityRecognizerArn: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    SubmitTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    TrainingStartTime: datetime.datetime | StrictStr | None = None
    TrainingEndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: ComprehendEntityRecognizerInputDataConfig | None = None
    RecognizerMetadata: ComprehendEntityRecognizerMetadata | None = None
    DataAccessRoleArn: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
    ModelKmsKeyId: StrictStr | None = None
    VersionName: StrictStr | None = None
    SourceModelArn: StrictStr | None = None
    FlywheelArn: StrictStr | None = None
    OutputDataConfig: ComprehendEntityRecognizerOutputDataConfig | None = None
