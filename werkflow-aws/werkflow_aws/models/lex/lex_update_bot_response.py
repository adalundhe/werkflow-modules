from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_member import LexBotMember
from .lex_data_privacy import LexDataPrivacy
from .lex_error_log_settings import LexErrorLogSettings


class LexUpdateBotResponse(BaseModel):
    botId: StrictStr | None = None
    botName: StrictStr | None = None
    description: StrictStr | None = None
    roleArn: StrictStr | None = None
    dataPrivacy: LexDataPrivacy | None = None
    idleSessionTTLInSeconds: StrictInt | None = None
    botStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    botType: StrictStr | None = None
    botMembers: list[LexBotMember] | None = None
    errorLogSettings: LexErrorLogSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
