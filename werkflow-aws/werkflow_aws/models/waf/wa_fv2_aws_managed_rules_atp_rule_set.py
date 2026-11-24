from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .wa_fv2_request_inspection import WAFv2RequestInspection
from .wa_fv2_response_inspection import WAFv2ResponseInspection


class WAFv2AWSManagedRulesATPRuleSet(BaseModel):
    LoginPath: StrictStr | None = None
    RequestInspection: WAFv2RequestInspection | None = None
    ResponseInspection: WAFv2ResponseInspection | None = None
    EnableRegexInPath: StrictBool | None = None
