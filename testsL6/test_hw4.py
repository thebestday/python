
from file import NameList

def test_1_func_NameList():
    list_name1 = ["Emily", "Emma", "Madison", "Olivia", "Hannah", "Abigail", "Isabella", "Ashley", "Samantha", "Elizabeth"]
    assert len(NameList(list_name1, 100)) == 100


def test_2_func_NameList():
    list_name2 = ["Emily", "Emma", "Madison", "Olivia", "Hannah", "Abigail", "Isabella", "Ashley", "Samantha","Elizabeth", "Alexis"]
    assert NameList(list_name2, 100) != NameList(list_name2, 100)









