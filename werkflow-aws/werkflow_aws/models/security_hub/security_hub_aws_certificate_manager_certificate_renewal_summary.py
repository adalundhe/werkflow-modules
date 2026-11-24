from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_certificate_manager_certificate_domain_validation_option import SecurityHubAwsCertificateManagerCertificateDomainValidationOption


class SecurityHubAwsCertificateManagerCertificateRenewalSummary(BaseModel):
    DomainValidationOptions: list[SecurityHubAwsCertificateManagerCertificateDomainValidationOption] | None = None
    RenewalStatus: StrictStr | None = None
    RenewalStatusReason: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
