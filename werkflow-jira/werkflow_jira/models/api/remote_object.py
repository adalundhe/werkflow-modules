from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .icon import Icon
from .status import Status


class RemoteObject(BaseModel):
    model_config = ConfigDict(extra="allow")

    icon: Icon | None = None
    status: Status | None = None
    summary: StrictStr | None = None
    title: StrictStr | None = None
    url: StrictStr | None = None
