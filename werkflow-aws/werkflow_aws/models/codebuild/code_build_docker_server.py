from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_docker_server_status import CodeBuildDockerServerStatus


class CodeBuildDockerServer(BaseModel):
    computeType: StrictStr | None = None
    securityGroupIds: list[StrictStr] | None = None
    status: CodeBuildDockerServerStatus | None = None
