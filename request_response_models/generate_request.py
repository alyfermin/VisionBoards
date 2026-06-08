from pydantic import BaseModel

class GenerateRequest(BaseModel):
    board_name: str
    inspo_keywords: list[str]