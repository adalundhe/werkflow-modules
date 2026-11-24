from __future__ import annotations
from pydantic import BaseModel
from .ssm_gcp_project import SSMGcpProject


class SSMGcpConfigurationTargets(BaseModel):
    Projects: list[SSMGcpProject] | None = None
