from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .acm_subject_alternative_name_filter import ACMSubjectAlternativeNameFilter
from .acm_subject_filter import ACMSubjectFilter
from .acm_timestamp_range import ACMTimestampRange


class ACMX509AttributeFilter(BaseModel):
    Subject: ACMSubjectFilter | None = None
    SubjectAlternativeName: ACMSubjectAlternativeNameFilter | None = None
    ExtendedKeyUsage: Literal['TLS_WEB_SERVER_AUTHENTICATION', 'TLS_WEB_CLIENT_AUTHENTICATION', 'CODE_SIGNING', 'EMAIL_PROTECTION', 'TIME_STAMPING', 'OCSP_SIGNING', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'ANY', 'NONE', 'CUSTOM'] | None = None
    KeyUsage: Literal['DIGITAL_SIGNATURE', 'NON_REPUDIATION', 'KEY_ENCIPHERMENT', 'DATA_ENCIPHERMENT', 'KEY_AGREEMENT', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'ENCIPHER_ONLY', 'DECIPHER_ONLY', 'ANY', 'CUSTOM'] | None = None
    KeyAlgorithm: Literal['RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1'] | None = None
    SerialNumber: StrictStr | None = None
    NotAfter: ACMTimestampRange | None = None
    NotBefore: ACMTimestampRange | None = None
