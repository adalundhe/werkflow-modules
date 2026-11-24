from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_custom_attribute import ACMCustomAttribute


class ACMDistinguishedName(BaseModel):
    CommonName: StrictStr | None = None
    DomainComponents: list[StrictStr] | None = None
    Country: StrictStr | None = None
    CustomAttributes: list[ACMCustomAttribute] | None = None
    DistinguishedNameQualifier: StrictStr | None = None
    GenerationQualifier: StrictStr | None = None
    GivenName: StrictStr | None = None
    Initials: StrictStr | None = None
    Locality: StrictStr | None = None
    Organization: StrictStr | None = None
    OrganizationalUnit: StrictStr | None = None
    Pseudonym: StrictStr | None = None
    SerialNumber: StrictStr | None = None
    State: StrictStr | None = None
    Surname: StrictStr | None = None
    Title: StrictStr | None = None
