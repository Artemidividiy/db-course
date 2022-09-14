from enum import Enum
import rich

class Param(Enum):
    country = 0
    emploee = 1
    emploees_stocks = 2
    item = 3
    organization = 4
    place = 5
    position = 6
    priority = 7
    stock = 8
    _type = 9

def convert_param_enum_to_str(param: Param) -> str:
    if param == Param.country: return "countries"
    if param == Param.emploee: return "emploees"
    if param == Param.emploees_stocks: return "emploees_stocks"
    if param == Param.item: return "items"
    if param == Param.organization: return "organizations"
    if param == Param.place: return "places"
    if param == Param.position: return "positions"
    if param == Param.priority: return "priorities"
    if param == Param.stock: return "stocks"
    if param == Param._type: return "types"
    rich.console.Console().log("enum not found")

def convert_str_to_param_enum(param: str) -> Param: 
    if param == "countries": return Param.country
    if param == "emploees": return Param.emploee
    if param ==  "emploees_stocks": return Param.emploees_stocks
    if param ==  "items": return Param.item
    if param ==  "organizations": return Param.organization
    if param ==  "places": return Param.place
    if param ==  "positions": return Param.position
    if param ==  "priorities": return Param.priority
    if param ==  "stocks": return Param.stock
    if param ==  "types": return Param._type
    rich.console.Console().log("given string does not match any enum field")