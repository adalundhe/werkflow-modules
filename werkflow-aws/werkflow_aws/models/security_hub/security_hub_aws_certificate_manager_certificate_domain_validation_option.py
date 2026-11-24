from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_certificate_manager_certificate_resource_record import SecurityHubAwsCertificateManagerCertificateResourceRecord


class SecurityHubAwsCertificateManagerCertificateDomainValidationOption(BaseModel):
    DomainName: StrictStr | None = None
    ResourceRecord: SecurityHubAwsCertificateManagerCertificateResourceRecord | None = None
    ValidationDomain: StrictStr | None = None
    ValidationEmails: list[StrictStr] | None = None
    ValidationMethod: StrictStr | None = None
    ValidationStatus: StrictStr | None = None
