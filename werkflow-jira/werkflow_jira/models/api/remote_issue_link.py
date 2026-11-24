from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .application import Application
from .remote_object import RemoteObject


class RemoteIssueLink(BaseModel):
    application: Application | None = None
    globalId: StrictStr | None = None
    id: StrictInt | None = None
    object: RemoteObject | None = None
    relationship: StrictStr | None = None
    self: StrictStr | None = None
