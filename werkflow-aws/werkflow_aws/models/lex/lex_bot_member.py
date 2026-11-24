from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBotMember(BaseModel):
    botMemberId: StrictStr | None = None
    botMemberName: StrictStr | None = None
    botMemberAliasId: StrictStr | None = None
    botMemberAliasName: StrictStr | None = None
    botMemberVersion: StrictStr | None = None
