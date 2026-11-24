from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_distinguished_name import ACMDistinguishedName
from .acm_general_name import ACMGeneralName


class ACMX509Attributes(BaseModel):
    Issuer: ACMDistinguishedName | None = None
    Subject: ACMDistinguishedName | None = None
    SubjectAlternativeNames: list[ACMGeneralName] | None = None
    ExtendedKeyUsages: list[StrictStr] | None = None
    KeyAlgorithm: StrictStr | None = None
    KeyUsages: list[StrictStr] | None = None
    SerialNumber: StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    NotBefore: datetime.datetime | StrictStr | None = None
