from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyWebhook(BaseModel):
    webhookArn: StrictStr | None = None
    webhookId: StrictStr | None = None
    webhookUrl: StrictStr | None = None
    appId: StrictStr | None = None
    branchName: StrictStr | None = None
    description: StrictStr | None = None
    createTime: datetime.datetime | StrictStr | None = None
    updateTime: datetime.datetime | StrictStr | None = None
