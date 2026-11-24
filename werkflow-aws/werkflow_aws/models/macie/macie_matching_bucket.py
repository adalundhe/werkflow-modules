from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_job_details import MacieJobDetails
from .macie_object_count_by_encryption_type import MacieObjectCountByEncryptionType
from .macie_object_level_statistics import MacieObjectLevelStatistics


class MacieMatchingBucket(BaseModel):
    accountId: StrictStr | None = None
    automatedDiscoveryMonitoringStatus: StrictStr | None = None
    bucketName: StrictStr | None = None
    classifiableObjectCount: StrictInt | None = None
    classifiableSizeInBytes: StrictInt | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
    jobDetails: MacieJobDetails | None = None
    lastAutomatedDiscoveryTime: datetime.datetime | StrictStr | None = None
    objectCount: StrictInt | None = None
    objectCountByEncryptionType: MacieObjectCountByEncryptionType | None = None
    sensitivityScore: StrictInt | None = None
    sizeInBytes: StrictInt | None = None
    sizeInBytesCompressed: StrictInt | None = None
    unclassifiableObjectCount: MacieObjectLevelStatistics | None = None
    unclassifiableObjectSizeInBytes: MacieObjectLevelStatistics | None = None
