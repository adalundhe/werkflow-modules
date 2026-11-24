from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_member_data_source_configuration import GuardDutyMemberDataSourceConfiguration
from .guard_duty_unprocessed_account import GuardDutyUnprocessedAccount


class GuardDutyGetMemberDetectorsResponse(BaseModel):
    MemberDataSourceConfigurations: list[GuardDutyMemberDataSourceConfiguration] | None = None
    UnprocessedAccounts: list[GuardDutyUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
