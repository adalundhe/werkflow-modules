from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_host_header_condition_config import ELBv2HostHeaderConditionConfig
from .el_bv2_http_header_condition_config import ELBv2HttpHeaderConditionConfig
from .el_bv2_http_request_method_condition_config import ELBv2HttpRequestMethodConditionConfig
from .el_bv2_path_pattern_condition_config import ELBv2PathPatternConditionConfig
from .el_bv2_query_string_condition_config import ELBv2QueryStringConditionConfig
from .el_bv2_source_ip_condition_config import ELBv2SourceIpConditionConfig


class ELBv2RuleCondition(BaseModel):
    Field: StrictStr | None = None
    Values: list[StrictStr] | None = None
    HostHeaderConfig: ELBv2HostHeaderConditionConfig | None = None
    PathPatternConfig: ELBv2PathPatternConditionConfig | None = None
    HttpHeaderConfig: ELBv2HttpHeaderConditionConfig | None = None
    QueryStringConfig: ELBv2QueryStringConditionConfig | None = None
    HttpRequestMethodConfig: ELBv2HttpRequestMethodConditionConfig | None = None
    SourceIpConfig: ELBv2SourceIpConditionConfig | None = None
    RegexValues: list[StrictStr] | None = None
