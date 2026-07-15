class GitHubAPIException(Exception):
    """Base exception class for all GitHub API-related issues."""
    pass

class GitHubUserNotFoundError(GitHubAPIException):
    """Raised when the requested GitHub username does not exist (Status 404)."""
    pass

class GitHubRateLimitExceededError(GitHubAPIException):
    """Raised when the GitHub API rate limit has been hit (Status 403)."""
    pass