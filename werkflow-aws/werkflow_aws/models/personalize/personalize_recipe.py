from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeRecipe(BaseModel):
    name: StrictStr | None = None
    recipeArn: StrictStr | None = None
    algorithmArn: StrictStr | None = None
    featureTransformationArn: StrictStr | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    recipeType: StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
