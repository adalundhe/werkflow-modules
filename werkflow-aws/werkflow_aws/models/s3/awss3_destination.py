from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_access_control_translation import AWSS3AccessControlTranslation
from .awss3_encryption_configuration import AWSS3EncryptionConfiguration
from .awss3_metrics import AWSS3Metrics
from .awss3_replication_time import AWSS3ReplicationTime


class AWSS3Destination(BaseModel):
    Bucket: StrictStr | None = None
    Account: StrictStr | None = None
    StorageClass: StrictStr | None = None
    AccessControlTranslation: AWSS3AccessControlTranslation | None = None
    EncryptionConfiguration: AWSS3EncryptionConfiguration | None = None
    ReplicationTime: AWSS3ReplicationTime | None = None
    Metrics: AWSS3Metrics | None = None
