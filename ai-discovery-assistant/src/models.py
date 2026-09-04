from pydantic import BaseModel


class DiscoveryAnalysis(BaseModel):
    clear: list[str]
    missing_information: list[str]
    discovery_questions: list[str]
    summary: str