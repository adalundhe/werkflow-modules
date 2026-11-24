from __future__ import annotations
from pydantic import BaseModel
from .route53_change_info import Route53ChangeInfo


class Route53GetChangeResponse(BaseModel):
    ChangeInfo: Route53ChangeInfo | None = None
