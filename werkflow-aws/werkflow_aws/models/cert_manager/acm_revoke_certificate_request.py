from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ACMRevokeCertificateRequest(BaseModel):
    CertificateArn: StrictStr
    RevocationReason: Literal['UNSPECIFIED', 'KEY_COMPROMISE', 'CA_COMPROMISE', 'AFFILIATION_CHANGED', 'SUPERCEDED', 'SUPERSEDED', 'CESSATION_OF_OPERATION', 'CERTIFICATE_HOLD', 'REMOVE_FROM_CRL', 'PRIVILEGE_WITHDRAWN', 'A_A_COMPROMISE']
