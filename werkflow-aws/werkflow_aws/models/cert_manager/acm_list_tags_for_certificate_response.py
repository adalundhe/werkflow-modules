from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acm_tag import ACMTag


class ACMListTagsForCertificateResponse(BaseModel):
    Tags: list[ACMTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
