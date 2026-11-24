from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .identity_store_external_id import IdentityStoreExternalId


class IdentityStoreGroup(BaseModel):
    IdentityStoreId: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupArn: StrictStr | None = None
    Revision: StrictStr | None = None
    DisplayName: StrictStr | None = None
    ExternalIds: list[IdentityStoreExternalId] | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    UpdatedBy: StrictStr | None = None
