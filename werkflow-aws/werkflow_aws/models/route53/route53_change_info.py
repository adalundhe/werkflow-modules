from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .route53_change_status import Route53ChangeStatus


class Route53ChangeInfo(BaseModel):
    Id: StrictStr | None = None
    Status: Route53ChangeStatus | None = None
    SubmittedAt: datetime.datetime | None = None
    Comment: StrictStr | None = None
