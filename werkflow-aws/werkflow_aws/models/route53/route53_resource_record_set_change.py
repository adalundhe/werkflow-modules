from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_model import Route53ResourceRecordSetModel


class Route53ResourceRecordSetChange(BaseModel):
    ChangeId: StrictStr | None = None
    Operation: StrictStr | None = None
    SubmittedAt: datetime.datetime | StrictStr | None = None
    SubmittedBy: StrictStr | None = None
    RequestId: StrictStr | None = None
    Action: StrictStr | None = None
    ResourceRecordSet: Route53ResourceRecordSetModel | None = None
