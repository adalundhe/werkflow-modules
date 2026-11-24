from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_certificate_manager_certificate_domain_validation_option import SecurityHubAwsCertificateManagerCertificateDomainValidationOption
from .security_hub_aws_certificate_manager_certificate_extended_key_usage import SecurityHubAwsCertificateManagerCertificateExtendedKeyUsage
from .security_hub_aws_certificate_manager_certificate_key_usage import SecurityHubAwsCertificateManagerCertificateKeyUsage
from .security_hub_aws_certificate_manager_certificate_options import SecurityHubAwsCertificateManagerCertificateOptions
from .security_hub_aws_certificate_manager_certificate_renewal_summary import SecurityHubAwsCertificateManagerCertificateRenewalSummary


class SecurityHubAwsCertificateManagerCertificateDetails(BaseModel):
    CertificateAuthorityArn: StrictStr | None = None
    CreatedAt: StrictStr | None = None
    DomainName: StrictStr | None = None
    DomainValidationOptions: list[SecurityHubAwsCertificateManagerCertificateDomainValidationOption] | None = None
    ExtendedKeyUsages: list[SecurityHubAwsCertificateManagerCertificateExtendedKeyUsage] | None = None
    FailureReason: StrictStr | None = None
    ImportedAt: StrictStr | None = None
    InUseBy: list[StrictStr] | None = None
    IssuedAt: StrictStr | None = None
    Issuer: StrictStr | None = None
    KeyAlgorithm: StrictStr | None = None
    KeyUsages: list[SecurityHubAwsCertificateManagerCertificateKeyUsage] | None = None
    NotAfter: StrictStr | None = None
    NotBefore: StrictStr | None = None
    Options: SecurityHubAwsCertificateManagerCertificateOptions | None = None
    RenewalEligibility: StrictStr | None = None
    RenewalSummary: SecurityHubAwsCertificateManagerCertificateRenewalSummary | None = None
    Serial: StrictStr | None = None
    SignatureAlgorithm: StrictStr | None = None
    Status: StrictStr | None = None
    Subject: StrictStr | None = None
    SubjectAlternativeNames: list[StrictStr] | None = None
    Type: StrictStr | None = None
