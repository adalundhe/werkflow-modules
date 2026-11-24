from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSelfManagedActiveDirectoryConfigurationUpdates(BaseModel):
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
    DnsIps: list[StrictStr] | None = None
    DomainName: StrictStr | None = None
    OrganizationalUnitDistinguishedName: StrictStr | None = None
    FileSystemAdministratorsGroup: StrictStr | None = None
    DomainJoinServiceAccountSecret: StrictStr | None = None
