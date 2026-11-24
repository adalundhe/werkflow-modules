from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_fulfillment_updates_specification import LexFulfillmentUpdatesSpecification
from .lex_post_fulfillment_status_specification import LexPostFulfillmentStatusSpecification


class LexFulfillmentCodeHookSettings(BaseModel):
    enabled: StrictBool | None = None
    postFulfillmentStatusSpecification: LexPostFulfillmentStatusSpecification | None = None
    fulfillmentUpdatesSpecification: LexFulfillmentUpdatesSpecification | None = None
    active: StrictBool | None = None
