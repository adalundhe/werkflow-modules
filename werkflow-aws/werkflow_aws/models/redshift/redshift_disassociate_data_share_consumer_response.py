from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_data_share_association import RedshiftDataShareAssociation


class RedshiftDisassociateDataShareConsumerResponse(BaseModel):
    DataShareArn: StrictStr | None = None
    ProducerArn: StrictStr | None = None
    AllowPubliclyAccessibleConsumers: StrictBool | None = None
    DataShareAssociations: list[RedshiftDataShareAssociation] | None = None
    ManagedBy: StrictStr | None = None
    DataShareType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
