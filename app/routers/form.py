from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

# POST endpoint to submit a form
@router.post("/form/submit", response_model=schemas.FormResponseSchema)
def submit_form(form: schemas.FormSubmitSchema, db: Session = Depends(get_db)):
    form_obj = models.KPAForm(**form.dict())
    db.add(form_obj)
    db.commit()
    db.refresh(form_obj)
    return form_obj

# GET endpoint to fetch all forms by user ID
@router.get("/form/fetchAllByUserId/{user_id}", response_model=list[schemas.FormResponseSchema])
def get_forms_by_user(user_id: int, db: Session = Depends(get_db)):
    forms = db.query(models.KPAForm).filter(models.KPAForm.user_id == user_id).all()
    return forms
