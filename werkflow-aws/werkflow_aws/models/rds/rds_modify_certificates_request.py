from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSModifyCertificatesRequest(BaseModel):
    CertificateIdentifier: StrictStr | None = None
    RemoveCustomerOverride: StrictBool | None = None
