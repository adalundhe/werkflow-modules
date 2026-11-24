from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .wa_fv2_request_inspection_acfp import WAFv2RequestInspectionACFP
from .wa_fv2_response_inspection import WAFv2ResponseInspection


class WAFv2AWSManagedRulesACFPRuleSet(BaseModel):
    CreationPath: StrictStr | None = None
    RegistrationPagePath: StrictStr | None = None
    RequestInspection: WAFv2RequestInspectionACFP | None = None
    ResponseInspection: WAFv2ResponseInspection | None = None
    EnableRegexInPath: StrictBool | None = None
