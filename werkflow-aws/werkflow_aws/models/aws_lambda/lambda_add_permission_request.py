from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaAddPermissionRequest(BaseModel):
    FunctionName: StrictStr
    StatementId: StrictStr
    Action: StrictStr
    Principal: StrictStr
    SourceArn: StrictStr | None = None
    FunctionUrlAuthType: Literal['NONE', 'AWS_IAM'] | None = None
    InvokedViaFunctionUrl: StrictBool | None = None
    SourceAccount: StrictStr | None = None
    EventSourceToken: StrictStr | None = None
    Qualifier: StrictStr | None = None
    RevisionId: StrictStr | None = None
    PrincipalOrgID: StrictStr | None = None
