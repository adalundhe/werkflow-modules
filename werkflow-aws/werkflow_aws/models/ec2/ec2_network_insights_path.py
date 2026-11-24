from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_path_filter import EC2PathFilter
from .ec2_tag_model import EC2TagModel


class EC2NetworkInsightsPath(BaseModel):
    NetworkInsightsPathId: StrictStr | None = None
    NetworkInsightsPathArn: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    Source: StrictStr | None = None
    Destination: StrictStr | None = None
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    SourceIp: StrictStr | None = None
    DestinationIp: StrictStr | None = None
    Protocol: StrictStr | None = None
    DestinationPort: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
    FilterAtSource: EC2PathFilter | None = None
    FilterAtDestination: EC2PathFilter | None = None
