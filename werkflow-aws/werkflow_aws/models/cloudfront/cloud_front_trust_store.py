from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudFrontTrustStore(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    NumberOfCaCertificates: StrictInt | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Reason: StrictStr | None = None
    UseClientCertificateOCSPEndpoint: StrictBool | None = None
