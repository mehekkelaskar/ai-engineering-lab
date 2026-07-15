import sys
import logging
from pathlib import Path

# Ensuring your execution environment recognizes the parent package structure smoothly
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.config import AppConfig
from src.Github_Client import GitHubClient
from src.exceptions import GitHubAPIException

def setup_logging() -> None:
    """Configures system tracking rules to pipe outputs directly into your app.log file."""
    # Ensure logs folder workspace exists securely
    Path("logs").mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log", encoding="utf-8"),
            logging.StreamHandler(sys.stdout) # Concurrently reflects critical logs inside execution terminals
        ]
    )

def main() -> None:
    setup_logging()
    logging.info("Developer Profile Aggregator starting up...")
    
    try:
        # Load configuration secrets securely
        token = AppConfig.token()
        
        # Prompt user input interaction directly via the CLI
        username = input("\nEnter the GitHub username to analyze: ").strip()
        if not username:
            logging.warning("User submitted an empty input string. Exiting operational flow.")
            print("Username entry cannot be empty.")
            return

        logging.info(f"Initiating remote query actions for username profile: '{username}'")
        
        # Perform client initialization and query execution
        client = GitHubClient(token=token)
        profile = client.fetch_developer_profile(username)
        
        # Render clean formatting summary output block to terminal interface
        print("\n" + "="*40)
        print(f"Developer: {profile.username}")
        print(f"Repositories: {profile.public_repos_count}")
        print("Main languages:")
        for lang in profile.get_main_languages():
            print(f" - {lang}")
        print("Most active repositories:")
        # Sort repos by star metrics to evaluate top items
        sorted_repos = sorted(profile.repositories, key=lambda x: x.stars, reverse=True)
        for repo in sorted_repos[:3]:
            print(f" - {repo.name} ({repo.stars} ⭐)")
        print("="*40 + "\n")
        
        logging.info(f"Successfully processed profile summary for '{username}'.")
        
    except GitHubAPIException as api_err:
        logging.error(f"Targeted operational failure occurred: {str(api_err)}")
        print(f"\n[API Error]: {str(api_err)}")
    except Exception as unexpected_err:
        logging.critical(f"An unhandled execution crash occurred: {str(unexpected_err)}", exc_info=True)
        print(f"\n[System Error]: A critical backend crash occurred. Check logs/app.log for details.")

if __name__ == "__main__":
    main()