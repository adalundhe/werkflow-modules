from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMOpsMetadata(BaseModel):
    ResourceId: StrictStr | None = None
    OpsMetadataArn: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    LastModifiedUser: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
