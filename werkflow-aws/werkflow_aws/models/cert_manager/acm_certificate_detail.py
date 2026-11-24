from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_certificate_options import ACMCertificateOptions
from .acm_domain_validation import ACMDomainValidation
from .acm_extended_key_usage import ACMExtendedKeyUsage
from .acm_key_usage import ACMKeyUsage
from .acm_renewal_summary import ACMRenewalSummary
from .acm_update_summary import ACMUpdateSummary


class ACMCertificateDetail(BaseModel):
    CertificateArn: StrictStr | None = None
    DomainName: StrictStr | None = None
    SubjectAlternativeNames: list[StrictStr] | None = None
    ManagedBy: StrictStr | None = None
    DomainValidationOptions: list[ACMDomainValidation] | None = None
    Serial: StrictStr | None = None
    Subject: StrictStr | None = None
    Issuer: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    IssuedAt: datetime.datetime | StrictStr | None = None
    ImportedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    RevokedAt: datetime.datetime | StrictStr | None = None
    RevocationReason: StrictStr | None = None
    NotBefore: datetime.datetime | StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    KeyAlgorithm: StrictStr | None = None
    SignatureAlgorithm: StrictStr | None = None
    InUseBy: list[StrictStr] | None = None
    FailureReason: StrictStr | None = None
    Type: StrictStr | None = None
    RenewalSummary: ACMRenewalSummary | None = None
    KeyUsages: list[ACMKeyUsage] | None = None
    ExtendedKeyUsages: list[ACMExtendedKeyUsage] | None = None
    CertificateAuthorityArn: StrictStr | None = None
    RenewalEligibility: StrictStr | None = None
    Options: ACMCertificateOptions | None = None
    UpdateSummary: ACMUpdateSummary | None = None
    CertificateKeyPairOrigin: StrictStr | None = None
    AcmeEndpointArn: StrictStr | None = None
    AcmeAccountId: StrictStr | None = None
    CertificateUsage: StrictStr | None = None
    RootHierarchyType: StrictStr | None = None
