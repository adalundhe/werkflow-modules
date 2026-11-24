from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontCertificate(BaseModel):
    Arn: StrictStr | None = None
