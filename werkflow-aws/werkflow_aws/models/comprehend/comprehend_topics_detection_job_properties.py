from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_output_data_config import ComprehendOutputDataConfig
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendTopicsDetectionJobProperties(BaseModel):
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    JobName: StrictStr | None = None
    JobStatus: StrictStr | None = None
    Message: StrictStr | None = None
    SubmitTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: ComprehendInputDataConfig | None = None
    OutputDataConfig: ComprehendOutputDataConfig | None = None
    NumberOfTopics: StrictInt | None = None
    DataAccessRoleArn: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
