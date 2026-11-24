from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_approval_rule_template import CodeCommitApprovalRuleTemplate


class CodeCommitUpdateApprovalRuleTemplateNameResponse(BaseModel):
    approvalRuleTemplate: CodeCommitApprovalRuleTemplate | None = None
    ResponseMetadata: dict[str, Any] | None = None
