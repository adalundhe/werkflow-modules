from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2NetworkInsightsAccessScope(BaseModel):
    NetworkInsightsAccessScopeId: StrictStr | None = None
    NetworkInsightsAccessScopeArn: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    UpdatedDate: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
