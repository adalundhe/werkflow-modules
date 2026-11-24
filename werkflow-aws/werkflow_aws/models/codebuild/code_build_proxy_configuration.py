from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_fleet_proxy_rule import CodeBuildFleetProxyRule


class CodeBuildProxyConfiguration(BaseModel):
    defaultBehavior: StrictStr | None = None
    orderedProxyRules: list[CodeBuildFleetProxyRule] | None = None
