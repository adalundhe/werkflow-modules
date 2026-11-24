from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDomainJoinInfo(BaseModel):
    DirectoryName: StrictStr | None = None
    OrganizationalUnitDistinguishedName: StrictStr | None = None
