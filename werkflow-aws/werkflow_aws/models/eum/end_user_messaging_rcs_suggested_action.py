from __future__ import annotations
from pydantic import BaseModel
from .end_user_messaging_rcs_create_calendar_event_action import EndUserMessagingRcsCreateCalendarEventAction
from .end_user_messaging_rcs_dial_phone_action import EndUserMessagingRcsDialPhoneAction
from .end_user_messaging_rcs_open_url_action import EndUserMessagingRcsOpenUrlAction
from .end_user_messaging_rcs_reply_action import EndUserMessagingRcsReplyAction
from .end_user_messaging_rcs_request_location_action import EndUserMessagingRcsRequestLocationAction
from .end_user_messaging_rcs_show_location_action import EndUserMessagingRcsShowLocationAction


class EndUserMessagingRcsSuggestedAction(BaseModel):
    Reply: EndUserMessagingRcsReplyAction | None = None
    OpenUrl: EndUserMessagingRcsOpenUrlAction | None = None
    DialPhone: EndUserMessagingRcsDialPhoneAction | None = None
    ShowLocation: EndUserMessagingRcsShowLocationAction | None = None
    RequestLocation: EndUserMessagingRcsRequestLocationAction | None = None
    CreateCalendarEvent: EndUserMessagingRcsCreateCalendarEventAction | None = None
