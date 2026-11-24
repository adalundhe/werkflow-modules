from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_change import Route53Change


class Route53ChangeBatch(BaseModel):
    Changes: list[Route53Change]
    Comment: StrictStr | None = None
