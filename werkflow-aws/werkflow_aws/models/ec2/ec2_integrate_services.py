from __future__ import annotations
from pydantic import BaseModel
from .ec2_athena_integration import EC2AthenaIntegration


class EC2IntegrateServices(BaseModel):
    AthenaIntegrations: list[EC2AthenaIntegration] | None = None
