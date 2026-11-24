from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2RegisteredInstance(BaseModel):
    InstanceId: StrictStr | None = None
    SqlServerLicenseUsage: StrictStr | None = None
    HaStatus: StrictStr | None = None
    ProcessingStatus: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    SqlServerCredentials: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
