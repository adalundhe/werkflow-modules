from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_change_info_model import Route53ChangeInfoModel


class Route53AssociateVPCWithHostedZoneResponse(BaseModel):
    ChangeInfo: Route53ChangeInfoModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
