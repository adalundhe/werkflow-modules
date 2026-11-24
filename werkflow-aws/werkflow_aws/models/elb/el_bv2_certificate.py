from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ELBv2Certificate(BaseModel):
    CertificateArn: StrictStr | None = None
    IsDefault: StrictBool | None = None
