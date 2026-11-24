from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2RouteServer(BaseModel):
    RouteServerId: StrictStr | None = None
    AmazonSideAsn: StrictInt | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    PersistRoutesState: StrictStr | None = None
    PersistRoutesDuration: StrictInt | None = None
    SnsNotificationsEnabled: StrictBool | None = None
    SnsTopicArn: StrictStr | None = None
