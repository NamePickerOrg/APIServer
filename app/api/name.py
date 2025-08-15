# 抽选
from . import core
SEXFAVOR_ALL = NUMFAVOR_BOTH = -1
SEXFAVOR_BOY = NUMFAVOR_1 = 0
SEXFAVOR_GIRL = NUMFAVOR_2 = 1
SEXFAVOR_SPEC = 2

current_path = "app/names/default.csv"
c = core.Core(current_path)

def choose(name_list:str="default",sex_favor:int=SEXFAVOR_ALL,num_favor:int=NUMFAVOR_BOTH,allow_repeat:bool=False,num:int=1):
    c.load_names(f"app/names/{name_list}.csv")
    c.set_num_favor(num_favor)
    c.set_sex_favor(sex_favor)
    tmp = c.pick(num,allow_repeat)
    if tmp == ["nothing"]:
        print("oh fuck")
        return "nothing"
    else:
        return tmp