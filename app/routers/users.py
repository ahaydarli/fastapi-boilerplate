from fastapi import APIRouter, Query, Depends

from app.schemas import UserSchema

router = APIRouter(prefix='/users', tags=['users'])


class SearchArgs:
    def __init__(
            self,
            query: str = Query(''),
            limit: int = Query(10),
            page: int = Query(0),
    ):
        self.query = query
        self.limit = limit
        self.page = page


@router.get('/', summary="List of users", description="Page through a list of users")
def get_users(args: SearchArgs = Depends()):

    return {
        "message": "users"
    }


@router.post('/')
def create_user(user: UserSchema):
    return user
