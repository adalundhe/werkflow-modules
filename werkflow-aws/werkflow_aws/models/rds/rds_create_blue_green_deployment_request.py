from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel
from .rds_target_resource_configuration import RDSTargetResourceConfiguration


class RDSCreateBlueGreenDeploymentRequest(BaseModel):
    BlueGreenDeploymentName: StrictStr
    Source: StrictStr
    TargetEngineVersion: StrictStr | None = None
    TargetDBParameterGroupName: StrictStr | None = None
    TargetDBClusterParameterGroupName: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
    TargetDBInstanceClass: StrictStr | None = None
    UpgradeTargetStorageConfig: StrictBool | None = None
    TargetIops: StrictInt | None = None
    TargetStorageType: StrictStr | None = None
    TargetAllocatedStorage: StrictInt | None = None
    TargetStorageThroughput: StrictInt | None = None
    TargetResourceConfigurations: list[RDSTargetResourceConfiguration] | None = None
