from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDestinationToCreate(BaseModel):
    Region: StrictStr | None = None
    AvailabilityZoneName: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    RoleArn: StrictStr | None = None
