from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_change_model import Route53ChangeModel


class Route53ChangeBatchModel(BaseModel):
    Comment: StrictStr | None = None
    Changes: list[Route53ChangeModel] | None = None
