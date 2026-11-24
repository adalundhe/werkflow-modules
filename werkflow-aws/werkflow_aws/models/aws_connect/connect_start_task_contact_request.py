from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_reference import ConnectReference
from .connect_segment_attribute_value import ConnectSegmentAttributeValue
from .connect_task_attachment import ConnectTaskAttachment


class ConnectStartTaskContactRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    PreviousContactId: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    ScheduledTime: datetime.datetime | StrictStr | None = None
    TaskTemplateId: StrictStr | None = None
    QuickConnectId: StrictStr | None = None
    RelatedContactId: StrictStr | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    Attachments: list[ConnectTaskAttachment] | None = None
