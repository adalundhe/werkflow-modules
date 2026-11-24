from __future__ import annotations
from pydantic import BaseModel
from .route53_change_action import Route53ChangeAction
from .route53_resource_record_set import Route53ResourceRecordSet


class Route53Change(BaseModel):
    Action: Route53ChangeAction
    ResourceRecordSet: Route53ResourceRecordSet
