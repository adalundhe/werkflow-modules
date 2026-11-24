from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_conditional_split_activity import PinpointConditionalSplitActivity
from .pinpoint_contact_center_activity import PinpointContactCenterActivity
from .pinpoint_custom_message_activity import PinpointCustomMessageActivity
from .pinpoint_email_message_activity import PinpointEmailMessageActivity
from .pinpoint_holdout_activity import PinpointHoldoutActivity
from .pinpoint_multi_conditional_split_activity import PinpointMultiConditionalSplitActivity
from .pinpoint_push_message_activity import PinpointPushMessageActivity
from .pinpoint_random_split_activity import PinpointRandomSplitActivity
from .pinpoint_sms_message_activity import PinpointSMSMessageActivity
from .pinpoint_wait_activity import PinpointWaitActivity


class PinpointActivity(BaseModel):
    CUSTOM: PinpointCustomMessageActivity | None = None
    ConditionalSplit: PinpointConditionalSplitActivity | None = None
    Description: StrictStr | None = None
    EMAIL: PinpointEmailMessageActivity | None = None
    Holdout: PinpointHoldoutActivity | None = None
    MultiCondition: PinpointMultiConditionalSplitActivity | None = None
    PUSH: PinpointPushMessageActivity | None = None
    RandomSplit: PinpointRandomSplitActivity | None = None
    SMS: PinpointSMSMessageActivity | None = None
    Wait: PinpointWaitActivity | None = None
    ContactCenter: PinpointContactCenterActivity | None = None
