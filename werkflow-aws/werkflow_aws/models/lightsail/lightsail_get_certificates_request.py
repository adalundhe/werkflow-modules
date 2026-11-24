from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetCertificatesRequest(BaseModel):
    certificateStatuses: list[Literal['PENDING_VALIDATION', 'ISSUED', 'INACTIVE', 'EXPIRED', 'VALIDATION_TIMED_OUT', 'REVOKED', 'FAILED']] | None = None
    includeCertificateDetails: StrictBool | None = None
    certificateName: StrictStr | None = None
    pageToken: StrictStr | None = None
