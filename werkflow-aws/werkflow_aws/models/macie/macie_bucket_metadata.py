from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_bucket_public_access import MacieBucketPublicAccess
from .macie_bucket_server_side_encryption import MacieBucketServerSideEncryption
from .macie_job_details import MacieJobDetails
from .macie_key_value_pair import MacieKeyValuePair
from .macie_object_count_by_encryption_type import MacieObjectCountByEncryptionType
from .macie_object_level_statistics import MacieObjectLevelStatistics
from .macie_replication_details import MacieReplicationDetails


class MacieBucketMetadata(BaseModel):
    accountId: StrictStr | None = None
    allowsUnencryptedObjectUploads: StrictStr | None = None
    automatedDiscoveryMonitoringStatus: StrictStr | None = None
    bucketArn: StrictStr | None = None
    bucketCreatedAt: datetime.datetime | StrictStr | None = None
    bucketName: StrictStr | None = None
    classifiableObjectCount: StrictInt | None = None
    classifiableSizeInBytes: StrictInt | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
    jobDetails: MacieJobDetails | None = None
    lastAutomatedDiscoveryTime: datetime.datetime | StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
    objectCount: StrictInt | None = None
    objectCountByEncryptionType: MacieObjectCountByEncryptionType | None = None
    publicAccess: MacieBucketPublicAccess | None = None
    region: StrictStr | None = None
    replicationDetails: MacieReplicationDetails | None = None
    sensitivityScore: StrictInt | None = None
    serverSideEncryption: MacieBucketServerSideEncryption | None = None
    sharedAccess: StrictStr | None = None
    sizeInBytes: StrictInt | None = None
    sizeInBytesCompressed: StrictInt | None = None
    tags: list[MacieKeyValuePair] | None = None
    unclassifiableObjectCount: MacieObjectLevelStatistics | None = None
    unclassifiableObjectSizeInBytes: MacieObjectLevelStatistics | None = None
    versioning: StrictBool | None = None
