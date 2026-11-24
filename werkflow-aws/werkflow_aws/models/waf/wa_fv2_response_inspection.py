from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_response_inspection_body_contains import WAFv2ResponseInspectionBodyContains
from .wa_fv2_response_inspection_header import WAFv2ResponseInspectionHeader
from .wa_fv2_response_inspection_json import WAFv2ResponseInspectionJson
from .wa_fv2_response_inspection_status_code import WAFv2ResponseInspectionStatusCode


class WAFv2ResponseInspection(BaseModel):
    StatusCode: WAFv2ResponseInspectionStatusCode | None = None
    Header: WAFv2ResponseInspectionHeader | None = None
    BodyContains: WAFv2ResponseInspectionBodyContains | None = None
    Json: WAFv2ResponseInspectionJson | None = None
