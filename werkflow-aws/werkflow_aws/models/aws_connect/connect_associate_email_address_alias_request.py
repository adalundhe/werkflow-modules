from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_alias_configuration import ConnectAliasConfiguration


class ConnectAssociateEmailAddressAliasRequest(BaseModel):
    EmailAddressId: StrictStr
    InstanceId: StrictStr
    AliasConfiguration: ConnectAliasConfiguration
    ClientToken: StrictStr | None = None
