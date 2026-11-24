from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2VpcBlockPublicAccessExclusion(BaseModel):
    ExclusionId: StrictStr | None = None
    InternetGatewayExclusionMode: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    State: StrictStr | None = None
    Reason: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    DeletionTimestamp: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
