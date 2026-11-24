from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerAssociationSummary(BaseModel):
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    SourceType: StrictStr | None = None
    DestinationType: StrictStr | None = None
    AssociationType: StrictStr | None = None
    SourceName: StrictStr | None = None
    DestinationName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
