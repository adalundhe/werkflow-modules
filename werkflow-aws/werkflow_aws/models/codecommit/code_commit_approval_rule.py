from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_commit_origin_approval_rule_template import CodeCommitOriginApprovalRuleTemplate


class CodeCommitApprovalRule(BaseModel):
    approvalRuleId: StrictStr | None = None
    approvalRuleName: StrictStr | None = None
    approvalRuleContent: StrictStr | None = None
    ruleContentSha256: StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedUser: StrictStr | None = None
    originApprovalRuleTemplate: CodeCommitOriginApprovalRuleTemplate | None = None
