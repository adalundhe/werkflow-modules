from __future__ import annotations
from pydantic import BaseModel
from .el_bv2_rewrite_config import ELBv2RewriteConfig


class ELBv2UrlRewriteConfig(BaseModel):
    Rewrites: list[ELBv2RewriteConfig] | None = None
