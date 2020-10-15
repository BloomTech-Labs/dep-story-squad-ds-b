from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas


def create_submission(db: Session, mold: schemas.Submission):
    """Function that updates the remote database with a new Submission
    Arguments:
    ---

    `mold` Submission(Pydantic model) - submission schema object
    In this use case this is very similar to a casting mold thus it's variable name

    Returns:
    ---

    `db_submission` Submission(SQLAlchemy model) - database model object
    """
    db_submission = models.Submission(mold.SubmissionID, mold.CohortID,
                                      mold.StoryID, mold.StoryLength,
                                      mold.AverageWordLength,
                                      mold.NumberQuotes,
                                      mold.UniqueWordsNumber,
                                      mold.AdjectiveNumber, mold.SquadScore)
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission


def get_submissions_by_cohort(db: Session, cohort_id: int, limit: int = 1000):
    """Function that querys the `submissions` table for entries that match a
    specific cohort_id
    Arugments:
    ---

    `cohort_id` int - cohort identifier number
    `limit` int (Default: 1000) - max number of results to return from query

    Returns:
    ---

    `q` tuple - tuple containing query results in the standardized form
    e.g ((result1,)(result2,))
    """
    q = db.query(models.Submission).filter(
        models.Submission.CohortID == cohort_id).limit(limit).all()
    return q


def get_submissions_by_squad_score(db: Session,
                                   min_r: int = 0,
                                   max_r: int = 100000,
                                   limit: int = 1000):
    """Function queries for all submissions withing a range by squad score
    Arguments:
    ---

    `min_r` int - minimum range to include (inclusive)
    `max_r` int - maximum range to include (inclusive)
    `limit` int - maximum number or results to return

    Returns:
    ---

    `q` tuple - tuple containing query results in the standardized form
    e.g ((result1,)(result2,))
    """
    q = db.query(models.Submission).filter(
        and_(models.Submission.SquadScore >= min_r,
        models.Submission.SquadScore <= max_r))\
        .limit(limit).all()
    return q


def get_all_submissions(db: Session, limit: int = 1000):
    """Function that queries all entries in the submissions table
    Arguments:
    ---

    `limit` int - maximum number of results to return

    `
    NOTE: if value of this parameter is 0 then disregard limit and
    return ALL entries. (please use this feature with caution)
    `
    """
    if limit == 0:
        q = db.query(models.Submission).all()
    else:
        q = db.query(models.Submission).limit(limit).all()
    return q
