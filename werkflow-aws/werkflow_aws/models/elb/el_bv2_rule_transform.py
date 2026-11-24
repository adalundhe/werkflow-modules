from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_host_header_rewrite_config import ELBv2HostHeaderRewriteConfig
from .el_bv2_url_rewrite_config import ELBv2UrlRewriteConfig


class ELBv2RuleTransform(BaseModel):
    Type: StrictStr | None = None
    HostHeaderRewriteConfig: ELBv2HostHeaderRewriteConfig | None = None
    UrlRewriteConfig: ELBv2UrlRewriteConfig | None = None
