from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_certificate_authority_scheduled_events import EKSCertificateAuthorityScheduledEvents
from .eks_certificate_authority_validity import EKSCertificateAuthorityValidity


class EKSCertificateAuthority(BaseModel):
    id: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    activatedAt: datetime.datetime | StrictStr | None = None
    activatedBy: StrictStr | None = None
    signingStatus: StrictStr | None = None
    distributionStatus: StrictStr | None = None
    validity: EKSCertificateAuthorityValidity | None = None
    scheduledEvents: EKSCertificateAuthorityScheduledEvents | None = None
    rollbackAvailable: StrictBool | None = None
    data: StrictStr | None = None
