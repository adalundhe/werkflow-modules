from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sqs_list_message_move_tasks_result_entry import SQSListMessageMoveTasksResultEntry


class SQSListMessageMoveTasksResponse(BaseModel):
    Results: list[SQSListMessageMoveTasksResultEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
