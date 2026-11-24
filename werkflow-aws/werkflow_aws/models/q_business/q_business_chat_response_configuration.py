from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessChatResponseConfiguration(BaseModel):
    chatResponseConfigurationId: StrictStr | None = None
    chatResponseConfigurationArn: StrictStr | None = None
    displayName: StrictStr | None = None
    responseConfigurationSummary: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
