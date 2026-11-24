from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_model import Route53ResourceRecordSetModel


class Route53ChangeModel(BaseModel):
    Action: StrictStr | None = None
    ResourceRecordSet: Route53ResourceRecordSetModel | None = None
