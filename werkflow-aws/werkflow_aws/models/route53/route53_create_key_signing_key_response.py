from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_change_info_model import Route53ChangeInfoModel
from .route53_key_signing_key import Route53KeySigningKey


class Route53CreateKeySigningKeyResponse(BaseModel):
    ChangeInfo: Route53ChangeInfoModel | None = None
    KeySigningKey: Route53KeySigningKey | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
