from pydantic import BaseModel

# For incoming POST request
class FormSubmitSchema(BaseModel):
    user_id: int
    form_data: str

# For outgoing response
class FormResponseSchema(BaseModel):
    id: int
    user_id: int
    form_data: str

    class Config:
        orm_mode = True
