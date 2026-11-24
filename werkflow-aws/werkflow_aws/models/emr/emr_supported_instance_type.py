from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class EMRSupportedInstanceType(BaseModel):
    Type: StrictStr | None = None
    MemoryGB: StrictFloat | StrictInt | None = None
    StorageGB: StrictInt | None = None
    VCPU: StrictInt | None = None
    Is64BitsOnly: StrictBool | None = None
    InstanceFamilyId: StrictStr | None = None
    EbsOptimizedAvailable: StrictBool | None = None
    EbsOptimizedByDefault: StrictBool | None = None
    NumberOfDisks: StrictInt | None = None
    EbsStorageOnly: StrictBool | None = None
    Architecture: StrictStr | None = None
