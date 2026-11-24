from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_member import LexBotMember
from .lex_data_privacy import LexDataPrivacy
from .lex_error_log_settings import LexErrorLogSettings


class LexCreateBotRequest(BaseModel):
    botName: StrictStr
    roleArn: StrictStr
    dataPrivacy: LexDataPrivacy
    idleSessionTTLInSeconds: StrictInt
    description: StrictStr | None = None
    botTags: dict[StrictStr, StrictStr] | None = None
    testBotAliasTags: dict[StrictStr, StrictStr] | None = None
    botType: Literal['Bot', 'BotNetwork'] | None = None
    botMembers: list[LexBotMember] | None = None
    errorLogSettings: LexErrorLogSettings | None = None
