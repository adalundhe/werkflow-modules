from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSelfManagedActiveDirectoryConfiguration(BaseModel):
    DomainName: StrictStr
    DnsIps: list[StrictStr]
    OrganizationalUnitDistinguishedName: StrictStr | None = None
    FileSystemAdministratorsGroup: StrictStr | None = None
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
    DomainJoinServiceAccountSecret: StrictStr | None = None
