class Database:
    def __init__(self):
        # In-memory tables
        self.topics_db = []
        self.questions_db = []
        
        # ID counters
        self.topic_id_counter = 1
        self.question_id_counter = 1

    def add_topic(self, topic_data: dict) -> dict:
        # Assign unique sequential ID
        topic_data["id"] = self.topic_id_counter
        self.topics_db.append(topic_data)
        self.topic_id_counter += 1
        return topic_data

    def add_question(self, question_data: dict) -> dict:
        # Assign unique sequential ID
        question_data["id"] = self.question_id_counter
        self.questions_db.append(question_data)
        self.question_id_counter += 1
        return question_data

    def get_all_questions(self, technology: str = None, difficulty: str = None) -> list:
        filtered_questions = self.questions_db
        
        # Apply case-insensitive technology filter if provided
        if technology:
            filtered_questions = [
                q for q in filtered_questions 
                if q["technology"].lower() == technology.lower()
            ]
            
        # Apply case-insensitive difficulty filter if provided
        if difficulty:
            filtered_questions = [
                q for q in filtered_questions 
                if q["difficulty"].lower() == difficulty.lower()
            ]
            
        return filtered_questions

    def get_question_by_id(self, question_id: int) -> dict:
        for question in self.questions_db:
            if question["id"] == question_id:
                return question
        return None

    def update_question_by_id(self, question_id: int, updated_data: dict) -> dict:
        for idx, question in enumerate(self.questions_db):
            if question["id"] == question_id:
                # Keep the original IDs intact, update the rest
                updated_data["id"] = question_id
                updated_data["topic_id"] = question["topic_id"]
                self.questions_db[idx] = updated_data
                return updated_data
        return None

    def delete_question_by_id(self, question_id: int) -> bool:
        for idx, question in enumerate(self.questions_db):
            if question["id"] == question_id:
                self.questions_db.pop(idx)
                return True
        return False

# Global shared instance used across all endpoint routers
db = Database()