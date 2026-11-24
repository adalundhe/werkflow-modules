from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListImportJobsRequest(BaseModel):
    ImportDestinationType: Literal['SUPPRESSION_LIST', 'CONTACT_LIST'] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
