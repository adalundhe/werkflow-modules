from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_handshake_party import OrganizationsHandshakeParty
from .organizations_tag_model import OrganizationsTagModel


class OrganizationsInviteAccountToOrganizationRequest(BaseModel):
    Target: OrganizationsHandshakeParty
    Notes: StrictStr | None = None
    Tags: list[OrganizationsTagModel] | None = None
