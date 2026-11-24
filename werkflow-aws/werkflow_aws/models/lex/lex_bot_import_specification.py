from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_data_privacy import LexDataPrivacy
from .lex_error_log_settings import LexErrorLogSettings


class LexBotImportSpecification(BaseModel):
    botName: StrictStr | None = None
    roleArn: StrictStr | None = None
    dataPrivacy: LexDataPrivacy | None = None
    errorLogSettings: LexErrorLogSettings | None = None
    idleSessionTTLInSeconds: StrictInt | None = None
    botTags: dict[StrictStr, StrictStr] | None = None
    testBotAliasTags: dict[StrictStr, StrictStr] | None = None
