from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ACMFilters(BaseModel):
    extendedKeyUsage: list[Literal['TLS_WEB_SERVER_AUTHENTICATION', 'TLS_WEB_CLIENT_AUTHENTICATION', 'CODE_SIGNING', 'EMAIL_PROTECTION', 'TIME_STAMPING', 'OCSP_SIGNING', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'ANY', 'NONE', 'CUSTOM']] | None = None
    keyUsage: list[Literal['DIGITAL_SIGNATURE', 'NON_REPUDIATION', 'KEY_ENCIPHERMENT', 'DATA_ENCIPHERMENT', 'KEY_AGREEMENT', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'ENCIPHER_ONLY', 'DECIPHER_ONLY', 'ANY', 'CUSTOM']] | None = None
    keyTypes: list[Literal['RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1']] | None = None
    exportOption: Literal['ENABLED', 'DISABLED'] | None = None
    managedBy: Literal['CLOUDFRONT'] | None = None
