from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class CodeCommitClient(ABC):

    @abstractmethod
    def associate_approval_rule_template_with_repository(
        self,
        *,
        approvalRuleTemplateName: str,
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_approval_rule_template_with_repositories(
        self,
        *,
        approvalRuleTemplateName: str,
        repositoryNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        maxMergeHunks: int | None = None,
        maxConflictFiles: int | None = None,
        filePaths: list[str] | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_approval_rule_template_from_repositories(
        self,
        *,
        approvalRuleTemplateName: str,
        repositoryNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_commits(
        self,
        *,
        commitIds: list[str],
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_repositories(
        self,
        *,
        repositoryNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
        approvalRuleTemplateContent: str,
        approvalRuleTemplateDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_branch(
        self,
        *,
        repositoryName: str,
        branchName: str,
        commitId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_commit(
        self,
        *,
        repositoryName: str,
        branchName: str,
        parentCommitId: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        commitMessage: str | None = None,
        keepEmptyFolders: bool | None = None,
        putFiles: list[dict[str, Any]] | None = None,
        deleteFiles: list[dict[str, Any]] | None = None,
        setFileModes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pull_request(
        self,
        *,
        title: str,
        targets: list[dict[str, Any]],
        description: str | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pull_request_approval_rule(
        self,
        *,
        pullRequestId: str,
        approvalRuleName: str,
        approvalRuleContent: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_repository(
        self,
        *,
        repositoryName: str,
        repositoryDescription: str | None = None,
        tags: dict[str, str] | None = None,
        kmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_unreferenced_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        commitMessage: str | None = None,
        keepEmptyFolders: bool | None = None,
        conflictResolution: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_branch(
        self,
        *,
        repositoryName: str,
        branchName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_comment_content(
        self,
        *,
        commentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool | None = None,
        commitMessage: str | None = None,
        name: str | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pull_request_approval_rule(
        self,
        *,
        pullRequestId: str,
        approvalRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_repository(
        self,
        *,
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        filePath: str,
        maxMergeHunks: int | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pull_request_events(
        self,
        *,
        pullRequestId: str,
        pullRequestEventType: str | None = None,
        actorArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_approval_rule_template_from_repository(
        self,
        *,
        approvalRuleTemplateName: str,
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evaluate_pull_request_approval_rules(
        self,
        *,
        pullRequestId: str,
        revisionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blob(
        self,
        *,
        repositoryName: str,
        blobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blob_differences(
        self,
        *,
        repositoryName: str,
        afterBlobId: str,
        beforeBlobId: str | None = None,
        contextLines: int | None = None,
        ignoreWhitespace: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_branch(
        self,
        *,
        repositoryName: str | None = None,
        branchName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_comment(
        self,
        *,
        commentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_comment_reactions(
        self,
        *,
        commentId: str,
        reactionUserArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_comments_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_comments_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str | None = None,
        beforeCommitId: str | None = None,
        afterCommitId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_commit(
        self,
        *,
        repositoryName: str,
        commitId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_differences(
        self,
        *,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str | None = None,
        beforePath: str | None = None,
        afterPath: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_file(
        self,
        *,
        repositoryName: str,
        filePath: str,
        commitSpecifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_folder(
        self,
        *,
        repositoryName: str,
        folderPath: str,
        commitSpecifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: str | None = None,
        maxConflictFiles: int | None = None,
        conflictResolutionStrategy: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_merge_options(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pull_request(
        self,
        *,
        pullRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pull_request_approval_states(
        self,
        *,
        pullRequestId: str,
        revisionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pull_request_override_state(
        self,
        *,
        pullRequestId: str,
        revisionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository(
        self,
        *,
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository_triggers(
        self,
        *,
        repositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_approval_rule_templates(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_approval_rule_templates_for_repository(
        self,
        *,
        repositoryName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_branches(
        self,
        *,
        repositoryName: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_file_commit_history(
        self,
        *,
        repositoryName: str,
        filePath: str,
        commitSpecifier: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pull_requests(
        self,
        *,
        repositoryName: str,
        authorArn: str | None = None,
        pullRequestStatus: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_repositories(
        self,
        *,
        nextToken: str | None = None,
        sortBy: str | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_repositories_for_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_branches_by_fast_forward(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_branches_by_squash(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        commitMessage: str | None = None,
        keepEmptyFolders: bool | None = None,
        conflictResolution: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_branches_by_three_way(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        commitMessage: str | None = None,
        keepEmptyFolders: bool | None = None,
        conflictResolution: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_pull_request_by_fast_forward(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_pull_request_by_squash(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        commitMessage: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        keepEmptyFolders: bool | None = None,
        conflictResolution: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_pull_request_by_three_way(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str | None = None,
        conflictDetailLevel: str | None = None,
        conflictResolutionStrategy: str | None = None,
        commitMessage: str | None = None,
        authorName: str | None = None,
        email: str | None = None,
        keepEmptyFolders: bool | None = None,
        conflictResolution: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def override_pull_request_approval_rules(
        self,
        *,
        pullRequestId: str,
        revisionId: str,
        overrideStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def post_comment_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str | None = None,
        location: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def post_comment_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def post_comment_reply(
        self,
        *,
        inReplyTo: str,
        content: str,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_comment_reaction(
        self,
        *,
        commentId: str,
        reactionValue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        fileContent: bytes | BinaryIO | str,
        filePath: str,
        fileMode: str | None = None,
        parentCommitId: str | None = None,
        commitMessage: str | None = None,
        name: str | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_repository_triggers(
        self,
        *,
        repositoryName: str,
        triggers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_repository_triggers(
        self,
        *,
        repositoryName: str,
        triggers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_approval_rule_template_content(
        self,
        *,
        approvalRuleTemplateName: str,
        newRuleContent: str,
        existingRuleContentSha256: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_approval_rule_template_description(
        self,
        *,
        approvalRuleTemplateName: str,
        approvalRuleTemplateDescription: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_approval_rule_template_name(
        self,
        *,
        oldApprovalRuleTemplateName: str,
        newApprovalRuleTemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_comment(
        self,
        *,
        commentId: str,
        content: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_default_branch(
        self,
        *,
        repositoryName: str,
        defaultBranchName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_request_approval_rule_content(
        self,
        *,
        pullRequestId: str,
        approvalRuleName: str,
        newRuleContent: str,
        existingRuleContentSha256: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_request_approval_state(
        self,
        *,
        pullRequestId: str,
        revisionId: str,
        approvalState: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_request_description(
        self,
        *,
        pullRequestId: str,
        description: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_request_status(
        self,
        *,
        pullRequestId: str,
        pullRequestStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_request_title(
        self,
        *,
        pullRequestId: str,
        title: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_repository_description(
        self,
        *,
        repositoryName: str,
        repositoryDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_repository_encryption_key(
        self,
        *,
        repositoryName: str,
        kmsKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_repository_name(
        self,
        *,
        oldName: str,
        newName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
