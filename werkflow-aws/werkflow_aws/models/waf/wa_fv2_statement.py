from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .wa_fv2_asn_match_statement import WAFv2AsnMatchStatement
from .wa_fv2_byte_match_statement import WAFv2ByteMatchStatement
from .wa_fv2_geo_match_statement import WAFv2GeoMatchStatement
from .wa_fv2_ip_set_reference_statement import WAFv2IPSetReferenceStatement
from .wa_fv2_label_match_statement import WAFv2LabelMatchStatement
from .wa_fv2_managed_rule_group_statement import WAFv2ManagedRuleGroupStatement
from .wa_fv2_not_statement import WAFv2NotStatement
from .wa_fv2_or_statement import WAFv2OrStatement
from .wa_fv2_rate_based_statement import WAFv2RateBasedStatement
from .wa_fv2_regex_match_statement import WAFv2RegexMatchStatement
from .wa_fv2_regex_pattern_set_reference_statement import WAFv2RegexPatternSetReferenceStatement
from .wa_fv2_rule_group_reference_statement import WAFv2RuleGroupReferenceStatement
from .wa_fv2_size_constraint_statement import WAFv2SizeConstraintStatement
from .wa_fv2_sqli_match_statement import WAFv2SqliMatchStatement
from .wa_fv2_xss_match_statement import WAFv2XssMatchStatement

if TYPE_CHECKING:
    from .wa_fv2_and_statement import WAFv2AndStatement


class WAFv2Statement(BaseModel):
    ByteMatchStatement: WAFv2ByteMatchStatement | None = None
    SqliMatchStatement: WAFv2SqliMatchStatement | None = None
    XssMatchStatement: WAFv2XssMatchStatement | None = None
    SizeConstraintStatement: WAFv2SizeConstraintStatement | None = None
    GeoMatchStatement: WAFv2GeoMatchStatement | None = None
    RuleGroupReferenceStatement: WAFv2RuleGroupReferenceStatement | None = None
    IPSetReferenceStatement: WAFv2IPSetReferenceStatement | None = None
    RegexPatternSetReferenceStatement: WAFv2RegexPatternSetReferenceStatement | None = None
    RateBasedStatement: WAFv2RateBasedStatement | None = None
    AndStatement: WAFv2AndStatement | None = None
    OrStatement: WAFv2OrStatement | None = None
    NotStatement: WAFv2NotStatement | None = None
    ManagedRuleGroupStatement: WAFv2ManagedRuleGroupStatement | None = None
    LabelMatchStatement: WAFv2LabelMatchStatement | None = None
    RegexMatchStatement: WAFv2RegexMatchStatement | None = None
    AsnMatchStatement: WAFv2AsnMatchStatement | None = None
