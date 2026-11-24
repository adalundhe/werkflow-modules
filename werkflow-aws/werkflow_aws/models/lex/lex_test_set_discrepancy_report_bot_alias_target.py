from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTestSetDiscrepancyReportBotAliasTarget(BaseModel):
    botId: StrictStr | None = None
    botAliasId: StrictStr | None = None
    localeId: StrictStr | None = None
