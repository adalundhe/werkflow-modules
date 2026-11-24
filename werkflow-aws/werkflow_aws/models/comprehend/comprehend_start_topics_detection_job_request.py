from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_output_data_config import ComprehendOutputDataConfig
from .comprehend_tag import ComprehendTag
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendStartTopicsDetectionJobRequest(BaseModel):
    InputDataConfig: ComprehendInputDataConfig
    OutputDataConfig: ComprehendOutputDataConfig
    DataAccessRoleArn: StrictStr
    JobName: StrictStr | None = None
    NumberOfTopics: StrictInt | None = None
    ClientRequestToken: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
    Tags: list[ComprehendTag] | None = None
