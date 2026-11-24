from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSelfManagedActiveDirectoryAttributes(BaseModel):
    DomainName: StrictStr | None = None
    OrganizationalUnitDistinguishedName: StrictStr | None = None
    FileSystemAdministratorsGroup: StrictStr | None = None
    UserName: StrictStr | None = None
    DnsIps: list[StrictStr] | None = None
    DomainJoinServiceAccountSecret: StrictStr | None = None
