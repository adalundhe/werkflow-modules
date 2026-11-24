from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_alias_configuration import ConnectAliasConfiguration


class ConnectDescribeEmailAddressResponse(BaseModel):
    EmailAddressId: StrictStr | None = None
    EmailAddressArn: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    CreateTimestamp: StrictStr | None = None
    ModifiedTimestamp: StrictStr | None = None
    AliasConfigurations: list[ConnectAliasConfiguration] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
