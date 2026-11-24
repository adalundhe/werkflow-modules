from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CodeCommitComment(BaseModel):
    commentId: StrictStr | None = None
    content: StrictStr | None = None
    inReplyTo: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    authorArn: StrictStr | None = None
    deleted: StrictBool | None = None
    clientRequestToken: StrictStr | None = None
    callerReactions: list[StrictStr] | None = None
    reactionCounts: dict[StrictStr, StrictInt] | None = None
