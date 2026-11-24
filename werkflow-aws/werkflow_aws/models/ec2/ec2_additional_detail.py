from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_analysis_component import EC2AnalysisComponent
from .ec2_rule_group_rule_options_pair import EC2RuleGroupRuleOptionsPair
from .ec2_rule_group_type_pair import EC2RuleGroupTypePair
from .ec2_rule_option import EC2RuleOption


class EC2AdditionalDetail(BaseModel):
    AdditionalDetailType: StrictStr | None = None
    Component: EC2AnalysisComponent | None = None
    VpcEndpointService: EC2AnalysisComponent | None = None
    RuleOptions: list[EC2RuleOption] | None = None
    RuleGroupTypePairs: list[EC2RuleGroupTypePair] | None = None
    RuleGroupRuleOptionsPairs: list[EC2RuleGroupRuleOptionsPair] | None = None
    ServiceName: StrictStr | None = None
    LoadBalancers: list[EC2AnalysisComponent] | None = None
