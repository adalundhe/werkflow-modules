from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedAgreement(BaseModel):
    Arn: StrictStr | None = None
    AgreementId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    ServerId: StrictStr | None = None
    LocalProfileId: StrictStr | None = None
    PartnerProfileId: StrictStr | None = None
