from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .application import Application
from .remote_object import RemoteObject


class RemoteIssueLinkRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    application: Application | None = None
    globalId: StrictStr | None = None
    object: RemoteObject | None = None
    relationship: StrictStr | None = None
