from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStorageConnector(BaseModel):
    ConnectorType: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    Domains: list[StrictStr] | None = None
    DomainsRequireAdminConsent: list[StrictStr] | None = None
