from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_encryption_configuration import SecurityLakeDataLakeEncryptionConfiguration
from .security_lake_data_lake_lifecycle_configuration import SecurityLakeDataLakeLifecycleConfiguration
from .security_lake_data_lake_replication_configuration import SecurityLakeDataLakeReplicationConfiguration
from .security_lake_data_lake_update_status import SecurityLakeDataLakeUpdateStatus


class SecurityLakeDataLakeResource(BaseModel):
    createStatus: StrictStr | None = None
    dataLakeArn: StrictStr | None = None
    encryptionConfiguration: SecurityLakeDataLakeEncryptionConfiguration | None = None
    lifecycleConfiguration: SecurityLakeDataLakeLifecycleConfiguration | None = None
    region: StrictStr | None = None
    replicationConfiguration: SecurityLakeDataLakeReplicationConfiguration | None = None
    s3BucketArn: StrictStr | None = None
    updateStatus: SecurityLakeDataLakeUpdateStatus | None = None
