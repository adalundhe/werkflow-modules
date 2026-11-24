from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_member import LexBotMember
from .lex_data_privacy import LexDataPrivacy
from .lex_parent_bot_network import LexParentBotNetwork


class LexDescribeBotVersionResponse(BaseModel):
    botId: StrictStr | None = None
    botName: StrictStr | None = None
    botVersion: StrictStr | None = None
    description: StrictStr | None = None
    roleArn: StrictStr | None = None
    dataPrivacy: LexDataPrivacy | None = None
    idleSessionTTLInSeconds: StrictInt | None = None
    botStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    parentBotNetworks: list[LexParentBotNetwork] | None = None
    botType: StrictStr | None = None
    botMembers: list[LexBotMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None
