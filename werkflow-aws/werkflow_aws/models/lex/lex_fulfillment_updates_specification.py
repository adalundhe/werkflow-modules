from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .lex_fulfillment_start_response_specification import LexFulfillmentStartResponseSpecification
from .lex_fulfillment_update_response_specification import LexFulfillmentUpdateResponseSpecification


class LexFulfillmentUpdatesSpecification(BaseModel):
    active: StrictBool | None = None
    startResponse: LexFulfillmentStartResponseSpecification | None = None
    updateResponse: LexFulfillmentUpdateResponseSpecification | None = None
    timeoutInSeconds: StrictInt | None = None
