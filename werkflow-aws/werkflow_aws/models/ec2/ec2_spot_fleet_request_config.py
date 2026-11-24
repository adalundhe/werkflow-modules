from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_spot_fleet_request_config_data import EC2SpotFleetRequestConfigData
from .ec2_tag_model import EC2TagModel


class EC2SpotFleetRequestConfig(BaseModel):
    ActivityStatus: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    SpotFleetRequestConfig: EC2SpotFleetRequestConfigData | None = None
    SpotFleetRequestId: StrictStr | None = None
    SpotFleetRequestState: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
