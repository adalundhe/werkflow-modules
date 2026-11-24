from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_cidr_block_summary import Route53CidrBlockSummary


class Route53ListCidrBlocksResponse(BaseModel):
    NextToken: StrictStr | None = None
    CidrBlocks: list[Route53CidrBlockSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
