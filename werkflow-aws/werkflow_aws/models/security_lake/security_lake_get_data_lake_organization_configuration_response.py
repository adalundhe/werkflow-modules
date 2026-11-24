from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_lake_data_lake_auto_enable_new_account_configuration import SecurityLakeDataLakeAutoEnableNewAccountConfiguration


class SecurityLakeGetDataLakeOrganizationConfigurationResponse(BaseModel):
    autoEnableNewAccount: list[SecurityLakeDataLakeAutoEnableNewAccountConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
