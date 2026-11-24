from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2LaunchTemplateHibernationOptions(BaseModel):
    Configured: StrictBool | None = None
