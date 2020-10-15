from typing import Optional

from pydantic import BaseModel


class SubmissionModel(BaseModel):
    """Pydantic model used to define the schema of Submission
    SQLAlchemy Model"""
    SubmissionID: int
    CohortID: Optional[int]
    StoryID: int
    StoryLength: int
    AverageWordLength: float
    NumberQuotes: int
    UniqueWordsNumber: int
    AdjectiveNumber: int
    SquadScore: float

    class Config:
        """allows for direct access to the underling ORM data model
        for more information about Pydantic's private `Config` class see
        https://pydantic-docs.helpmanual.io/#config"""
        orm_mode = True
