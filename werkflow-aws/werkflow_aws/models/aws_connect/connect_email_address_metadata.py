from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_alias_configuration import ConnectAliasConfiguration


class ConnectEmailAddressMetadata(BaseModel):
    EmailAddressId: StrictStr | None = None
    EmailAddressArn: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    AliasConfigurations: list[ConnectAliasConfiguration] | None = None
