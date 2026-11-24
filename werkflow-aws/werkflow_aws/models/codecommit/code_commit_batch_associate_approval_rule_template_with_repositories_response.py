from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_batch_associate_approval_rule_template_with_repositories_error import CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesError


class CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesResponse(BaseModel):
    associatedRepositoryNames: list[StrictStr] | None = None
    errors: list[CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
