from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_aggregated_utterances_summary import LexAggregatedUtterancesSummary
from .lex_utterance_aggregation_duration import LexUtteranceAggregationDuration


class LexListAggregatedUtterancesResponse(BaseModel):
    botId: StrictStr | None = None
    botAliasId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    aggregationDuration: LexUtteranceAggregationDuration | None = None
    aggregationWindowStartTime: datetime.datetime | StrictStr | None = None
    aggregationWindowEndTime: datetime.datetime | StrictStr | None = None
    aggregationLastRefreshedDateTime: datetime.datetime | StrictStr | None = None
    aggregatedUtterancesSummaries: list[LexAggregatedUtterancesSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
