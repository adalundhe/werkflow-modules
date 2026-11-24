from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerDomainDetails(BaseModel):
    DomainArn: StrictStr | None = None
    DomainId: StrictStr | None = None
    DomainName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Url: StrictStr | None = None
