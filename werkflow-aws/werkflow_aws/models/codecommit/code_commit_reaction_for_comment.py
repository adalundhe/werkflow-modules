from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_commit_reaction_value_formats import CodeCommitReactionValueFormats


class CodeCommitReactionForComment(BaseModel):
    reaction: CodeCommitReactionValueFormats | None = None
    reactionUsers: list[StrictStr] | None = None
    reactionsFromDeletedUsersCount: StrictInt | None = None
