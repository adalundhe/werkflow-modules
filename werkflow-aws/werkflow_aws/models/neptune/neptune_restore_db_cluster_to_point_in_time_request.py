from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_serverless_v2_scaling_configuration import NeptuneServerlessV2ScalingConfiguration
from .neptune_tag import NeptuneTag


class NeptuneRestoreDBClusterToPointInTimeRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    SourceDBClusterIdentifier: StrictStr
    RestoreType: StrictStr | None = None
    RestoreToTime: datetime.datetime | StrictStr | None = None
    UseLatestRestorableTime: StrictBool | None = None
    Port: StrictInt | None = None
    DBSubnetGroupName: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Tags: list[NeptuneTag] | None = None
    KmsKeyId: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    ServerlessV2ScalingConfiguration: NeptuneServerlessV2ScalingConfiguration | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
