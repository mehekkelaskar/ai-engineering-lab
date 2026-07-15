from typing import List, Optional

class Repository:
    def __init__(self, name: str, language: Optional[str], stars: int):
        """Represents a single GitHub repository."""
        self.name: str = name
        self.language: str = language if language else "Unknown"
        self.stars: int = stars

class DeveloperProfile:
    def __init__(self, username: str, public_repos_count: int, repositories: List[Repository]):
        """Represents the compiled summary profile of a developer."""
        self.username: str = username
        self.public_repos_count: int = public_repos_count
        self.repositories: List[Repository] = repositories

    def get_main_languages(self) -> List[str]:
        """Analyzes repositories to extract unique dominant programming languages."""
        languages = set()
        for repo in self.repositories:
            if repo.language != "Unknown":
                languages.add(repo.language)
        return list(languages)