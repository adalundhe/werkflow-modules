from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMServerCertificateMetadata(BaseModel):
    Path: StrictStr | None = None
    ServerCertificateName: StrictStr | None = None
    ServerCertificateId: StrictStr | None = None
    Arn: StrictStr | None = None
    UploadDate: datetime.datetime | StrictStr | None = None
    Expiration: datetime.datetime | StrictStr | None = None
