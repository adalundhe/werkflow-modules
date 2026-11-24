from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_encryption_configuration import SecurityLakeDataLakeEncryptionConfiguration
from .security_lake_data_lake_lifecycle_configuration import SecurityLakeDataLakeLifecycleConfiguration
from .security_lake_data_lake_replication_configuration import SecurityLakeDataLakeReplicationConfiguration


class SecurityLakeDataLakeConfiguration(BaseModel):
    region: StrictStr
    encryptionConfiguration: SecurityLakeDataLakeEncryptionConfiguration | None = None
    lifecycleConfiguration: SecurityLakeDataLakeLifecycleConfiguration | None = None
    replicationConfiguration: SecurityLakeDataLakeReplicationConfiguration | None = None
