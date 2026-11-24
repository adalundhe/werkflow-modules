from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .detective_membership_datasources import DetectiveMembershipDatasources
from .detective_unprocessed_account import DetectiveUnprocessedAccount


class DetectiveBatchGetGraphMemberDatasourcesResponse(BaseModel):
    MemberDatasources: list[DetectiveMembershipDatasources] | None = None
    UnprocessedAccounts: list[DetectiveUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
