from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_command_filter import SSMCommandFilter


class SSMListCommandInvocationsRequest(BaseModel):
    CommandId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[SSMCommandFilter] | None = None
    Details: StrictBool | None = None
