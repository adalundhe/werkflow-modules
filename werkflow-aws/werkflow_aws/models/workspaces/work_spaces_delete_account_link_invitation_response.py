from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_account_link import WorkSpacesAccountLink


class WorkSpacesDeleteAccountLinkInvitationResponse(BaseModel):
    AccountLink: WorkSpacesAccountLink | None = None
    ResponseMetadata: dict[str, Any] | None = None
