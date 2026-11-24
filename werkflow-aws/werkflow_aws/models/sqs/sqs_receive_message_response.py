from __future__ import annotations
from pydantic import BaseModel
from .sqs_message import SQSMessage


class SQSReceiveMessageResponse(BaseModel):
    Messages: list[SQSMessage] | None = None
