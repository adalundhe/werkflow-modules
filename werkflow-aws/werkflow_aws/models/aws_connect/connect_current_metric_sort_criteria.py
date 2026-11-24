from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectCurrentMetricSortCriteria(BaseModel):
    SortByMetric: Literal['AGENTS_ONLINE', 'AGENTS_AVAILABLE', 'AGENTS_ON_CALL', 'AGENTS_NON_PRODUCTIVE', 'AGENTS_AFTER_CONTACT_WORK', 'AGENTS_ERROR', 'AGENTS_STAFFED', 'CONTACTS_IN_QUEUE', 'OLDEST_CONTACT_AGE', 'CONTACTS_SCHEDULED', 'AGENTS_ON_CONTACT', 'SLOTS_ACTIVE', 'SLOTS_AVAILABLE', 'ESTIMATED_WAIT_TIME'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
