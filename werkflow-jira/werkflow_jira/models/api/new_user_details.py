from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class NewUserDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    applicationKeys: list[StrictStr] | None = None
    displayName: StrictStr | None = None
    emailAddress: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    password: StrictStr | None = None
    products: list[StrictStr] | None = None
    self: StrictStr | None = None
