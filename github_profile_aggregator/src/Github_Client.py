import requests
from typing import List, Dict, Any
from src.exceptions import GitHubUserNotFoundError, GitHubRateLimitExceededError, GitHubAPIException
from src.models import Repository, DeveloperProfile

class GitHubClient:
    BASE_URL = "https://api.github.com/users/"

    def __init__(self, token: str):
        """Initializes the API client with secure request headers."""
        self.headers: Dict[str, str] = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _make_request(self, url: str) -> Any:
        """Internal helper to safely make HTTP GET requests and check for errors."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            # Explicitly catch known API status error limits
            if response.status_code == 404:
                raise GitHubUserNotFoundError(f"The profile target could not be found.")
            elif response.status_code == 403:
                raise GitHubRateLimitExceededError("GitHub API rate limit exceeded or access forbidden.")
            elif response.status_code != 200:
                raise GitHubAPIException(f"GitHub API responded with error code: {response.status_code}")
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise GitHubAPIException(f"Network communication failure: {str(e)}")

    def fetch_developer_profile(self, username: str) -> DeveloperProfile:
        """Orchestrates API calls to construct a clean DeveloperProfile object."""
        # 1. Fetch main profile metadata
        profile_url = f"{self.BASE_URL}{username}"
        profile_json = self._make_request(profile_url)
        
        # 2. Fetch associated repository metadata
        repos_url = f"{self.BASE_URL}{username}/repos"
        repos_json = self._make_request(repos_url)
        
        # 3. Transform repository JSON payload into a list of Repository objects
        repo_objects: List[Repository] = []
        for repo_data in repos_json:
            repo_objects.append(
                Repository(
                    name=repo_data.get("name", "Unnamed"),
                    language=repo_data.get("language"),
                    stars=repo_data.get("stargazers_count", 0)
                )
            )
            
        # 4. Construct and return final composite profile object
        return DeveloperProfile(
            username=profile_json.get("login", username),
            public_repos_count=profile_json.get("public_repos", 0),
            repositories=repo_objects
        )