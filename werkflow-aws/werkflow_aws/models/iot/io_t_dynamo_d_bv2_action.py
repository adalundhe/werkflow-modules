from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_put_item_input import IoTPutItemInput


class IoTDynamoDBv2Action(BaseModel):
    roleArn: StrictStr | None = None
    putItem: IoTPutItemInput | None = None
