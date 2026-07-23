# app/tools.py

def calculate_match_score(matching_skills: list[str], missing_skills: list[str]) -> float:
    """
    Tool function to calculate the exact candidate match score percentage.
    """
    total_skills = len(matching_skills) + len(missing_skills)
    if total_skills == 0:
        return 0.0
    
    score = (len(matching_skills) / total_skills) * 100
    return round(score, 2)