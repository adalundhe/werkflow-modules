from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCommitApprovalRuleTemplate(BaseModel):
    approvalRuleTemplateId: StrictStr | None = None
    approvalRuleTemplateName: StrictStr | None = None
    approvalRuleTemplateDescription: StrictStr | None = None
    approvalRuleTemplateContent: StrictStr | None = None
    ruleContentSha256: StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedUser: StrictStr | None = None
