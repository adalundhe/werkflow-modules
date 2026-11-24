from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_aggregated_utterances_filter import LexAggregatedUtterancesFilter
from .lex_aggregated_utterances_sort_by import LexAggregatedUtterancesSortBy
from .lex_utterance_aggregation_duration import LexUtteranceAggregationDuration


class LexListAggregatedUtterancesRequest(BaseModel):
    botId: StrictStr
    localeId: StrictStr
    aggregationDuration: LexUtteranceAggregationDuration
    botAliasId: StrictStr | None = None
    botVersion: StrictStr | None = None
    sortBy: LexAggregatedUtterancesSortBy | None = None
    filters: list[LexAggregatedUtterancesFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
