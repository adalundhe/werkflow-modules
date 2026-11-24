from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .organizations_handshake_party import OrganizationsHandshakeParty
from .organizations_handshake_resource import OrganizationsHandshakeResource


class OrganizationsHandshake(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Parties: list[OrganizationsHandshakeParty] | None = None
    State: StrictStr | None = None
    RequestedTimestamp: datetime.datetime | StrictStr | None = None
    ExpirationTimestamp: datetime.datetime | StrictStr | None = None
    Action: StrictStr | None = None
    Resources: list[OrganizationsHandshakeResource] | None = None
