from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListAttachmentNatConfigurationsRequest(BaseModel):
    CoreNetworkId: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    Filters: dict[StrictStr, list[StrictStr]] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
