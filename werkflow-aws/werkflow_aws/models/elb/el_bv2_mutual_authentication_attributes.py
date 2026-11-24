from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .el_bv2_client_certificate_identity_filter import ELBv2ClientCertificateIdentityFilter


class ELBv2MutualAuthenticationAttributes(BaseModel):
    Mode: StrictStr | None = None
    TrustStoreArn: StrictStr | None = None
    IgnoreClientCertificateExpiry: StrictBool | None = None
    TrustStoreAssociationStatus: StrictStr | None = None
    AdvertiseTrustStoreCaNames: StrictStr | None = None
    ClientCertificateIdentityFilters: list[ELBv2ClientCertificateIdentityFilter] | None = None
