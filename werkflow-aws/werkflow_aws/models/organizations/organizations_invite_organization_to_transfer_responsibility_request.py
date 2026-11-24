from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .organizations_handshake_party import OrganizationsHandshakeParty
from .organizations_tag_model import OrganizationsTagModel


class OrganizationsInviteOrganizationToTransferResponsibilityRequest(BaseModel):
    Type: Literal['BILLING']
    Target: OrganizationsHandshakeParty
    StartTimestamp: datetime.datetime | StrictStr
    SourceName: StrictStr
    Notes: StrictStr | None = None
    Tags: list[OrganizationsTagModel] | None = None
