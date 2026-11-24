from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .acm_certificate_options import ACMCertificateOptions
from .acm_domain_validation_option import ACMDomainValidationOption
from .acm_tag import ACMTag


class ACMRequestCertificateRequest(BaseModel):
    DomainName: StrictStr
    ValidationMethod: Literal['EMAIL', 'DNS', 'HTTP'] | None = None
    SubjectAlternativeNames: list[StrictStr] | None = None
    IdempotencyToken: StrictStr | None = None
    DomainValidationOptions: list[ACMDomainValidationOption] | None = None
    Options: ACMCertificateOptions | None = None
    CertificateAuthorityArn: StrictStr | None = None
    Tags: list[ACMTag] | None = None
    KeyAlgorithm: Literal['RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1'] | None = None
    ManagedBy: Literal['CLOUDFRONT'] | None = None
    CertificateUsage: Literal['CLIENT_AND_SERVER_AUTH', 'CLIENT_AUTH_ONLY'] | None = None
    RootHierarchyType: Literal['N2_AMAZON_MANAGED', 'N2_SFG2_AMAZON_MANAGED'] | None = None
