from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_bucket_count_by_effective_permission import MacieBucketCountByEffectivePermission
from .macie_bucket_count_by_encryption_type import MacieBucketCountByEncryptionType
from .macie_bucket_count_by_shared_access_type import MacieBucketCountBySharedAccessType
from .macie_bucket_count_policy_allows_unencrypted_object_uploads import MacieBucketCountPolicyAllowsUnencryptedObjectUploads
from .macie_bucket_statistics_by_sensitivity import MacieBucketStatisticsBySensitivity
from .macie_object_level_statistics import MacieObjectLevelStatistics


class MacieGetBucketStatisticsResponse(BaseModel):
    bucketCount: StrictInt | None = None
    bucketCountByEffectivePermission: MacieBucketCountByEffectivePermission | None = None
    bucketCountByEncryptionType: MacieBucketCountByEncryptionType | None = None
    bucketCountByObjectEncryptionRequirement: MacieBucketCountPolicyAllowsUnencryptedObjectUploads | None = None
    bucketCountBySharedAccessType: MacieBucketCountBySharedAccessType | None = None
    bucketStatisticsBySensitivity: MacieBucketStatisticsBySensitivity | None = None
    classifiableObjectCount: StrictInt | None = None
    classifiableSizeInBytes: StrictInt | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
    objectCount: StrictInt | None = None
    sizeInBytes: StrictInt | None = None
    sizeInBytesCompressed: StrictInt | None = None
    unclassifiableObjectCount: MacieObjectLevelStatistics | None = None
    unclassifiableObjectSizeInBytes: MacieObjectLevelStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
