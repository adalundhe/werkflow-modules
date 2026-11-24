from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2LaunchTemplateHibernationOptionsRequest(BaseModel):
    Configured: StrictBool | None = None
