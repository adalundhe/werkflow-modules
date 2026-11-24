from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt


class DashboardGadgetPosition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    column_position_of_the_gadget: StrictInt | None = PydanticField(default=None, alias='The column position of the gadget.')
    row_position_of_the_gadget: StrictInt | None = PydanticField(default=None, alias='The row position of the gadget.')
