from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_distinguished_name import ACMDistinguishedName
from .acm_other_name import ACMOtherName


class ACMGeneralName(BaseModel):
    DirectoryName: ACMDistinguishedName | None = None
    DnsName: StrictStr | None = None
    IpAddress: StrictStr | None = None
    OtherName: ACMOtherName | None = None
    RegisteredId: StrictStr | None = None
    Rfc822Name: StrictStr | None = None
    UniformResourceIdentifier: StrictStr | None = None
