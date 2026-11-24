from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListAssociationsRequest(BaseModel):
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    SourceType: StrictStr | None = None
    DestinationType: StrictStr | None = None
    AssociationType: Literal['ContributedTo', 'AssociatedWith', 'DerivedFrom', 'Produced', 'SameAs'] | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['SourceArn', 'DestinationArn', 'SourceType', 'DestinationType', 'CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
