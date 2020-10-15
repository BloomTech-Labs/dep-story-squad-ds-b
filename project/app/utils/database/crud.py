from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas


def create_submission(db: Session, mold: schemas.Submission):
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


def get_submissions_by_cohort(db: Session, cohort_id: int, limit: int = 100):
    q = db.query(models.Submission).filter(
        models.Submission.CohortID == cohort_id).limit(limit).all()
    return q


def get_submissions_by_squad_score(db: Session,
                                   min_r: int = 0,
                                   max_r: int = 100000,
                                   limit: int = 1000):
    q = db.query(models.Submission).filter(
        and_(models.Submission.SquadScore < min_r,
        models.Submission.SquadScore > max_r))\
        .limit(limit).all()
    return q


def get_all_submissions(db: Session, limit: int = 1000):
    if limit == 0:
        q = db.query(models.Submission).all()
    else:
        q = db.query(models.Submission).limit(limit).all()
    return q
