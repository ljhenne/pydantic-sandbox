from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int


if __name__ == "__main__":
    p = Point(x=2,y=2)
    p_dict1 = p.dict()
    p_dict2 = p.dict()
    
    assert id(p_dict1) == id(p_dict2), "Pydantic generates a different dictionary with every .dict() call"

