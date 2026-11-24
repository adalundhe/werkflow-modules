from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_serverless_v2_scaling_configuration import DocumentDBServerlessV2ScalingConfiguration
from .document_db_tag import DocumentDBTag


class DocumentDBRestoreDBClusterToPointInTimeRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    SourceDBClusterIdentifier: StrictStr
    RestoreType: StrictStr | None = None
    RestoreToTime: datetime.datetime | StrictStr | None = None
    UseLatestRestorableTime: StrictBool | None = None
    Port: StrictInt | None = None
    DBSubnetGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Tags: list[DocumentDBTag] | None = None
    KmsKeyId: StrictStr | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    ServerlessV2ScalingConfiguration: DocumentDBServerlessV2ScalingConfiguration | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
