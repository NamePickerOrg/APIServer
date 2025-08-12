# NamePicker 核心（不直接开放API）
import random
import os

SEXFAVOR_ALL = NUMFAVOR_BOTH = -1
SEXFAVOR_BOY = NUMFAVOR_1 = 0
SEXFAVOR_GIRL = NUMFAVOR_2 = 1
SEXFAVOR_SPEC = 2

class Choose:
    def __init__(self,path:str):
        self.names = []
        self.namel = []
        self.sex = [[],[],[]]
        self.num = [[],[],[]]
        self.chosen = []
        self.sexFavor = SEXFAVOR_ALL
        self.numFavor = NUMFAVOR_BOTH
        self.load_names(path)

    def load_names(self,path:str) -> None:
        try:
            self.names = []
            self.namel = []
            with open(path,"r",encoding="utf-8") as f:
                fl = f.readlines()
            head = fl[0].strip("\n").split(",")
            del fl[0]
            for i in range(len(fl)):
                l = fl[i].strip("\n").split(",")
                struct = {}
                for j in range(len(head)):
                    struct[head[j]] = l[j]
                self.names.append(struct)
                self.namel.append(i)
        except (UnicodeDecodeError,IndexError):
            os.remove(path)
            if not os.path.exists("names"):
                os.makedirs("names")
            with open(path,"w",encoding="utf-8") as f:
                f.write("name,sex,no\n某人,0,1")
        except FileNotFoundError:
            if not os.path.exists("names"):
                os.makedirs("names")
            with open(path,"w",encoding="utf-8") as f:
                f.write("name,sex,no\n某人,0,1")

    def load_favor(self) -> None:
        self.namel = []
        for i in range(len(self.names)):
            self.namel.append(i)
        for i in range(len(self.namel)):
            if self.sexFavor == SEXFAVOR_ALL and self.numFavor == NUMFAVOR_BOTH:
                break
            else:
                if ((int(self.names[i]["sex"]) != self.sexFavor)
                or (int(self.names[i]["no"])%2 == 0 and self.numFavor==NUMFAVOR_1) 
                or (int(self.names[i]["no"])%2 == 1 and self.numFavor==NUMFAVOR_2)):
                    del self.namel[i]

    def set_sex_favor(self,target:int) -> None:
        self.sexFavor = target
        self.load_favor()

    def set_num_favor(self,target:int) -> None:
        self.numFavor = target
        self.load_favor()

    def pick(self,num:int=1,allow_repeat:bool=False) -> list:
        resi = []
        res = []
        for i in range(num):
            if not allow_repeat and not self.namel==[]:
                ans = random.choice(self.namel)
                resi.append(self.namel[self.namel.index(ans)])
                del self.namel[self.namel.index(ans)]
                continue
            elif not allow_repeat and self.namel==[]:
                self.load_favor()
                ans = random.choice(self.namel)
            else:
                ans = random.choice(self.namel)
            resi.append(self.namel[self.namel.index(ans)])

        for i in resi:
            res.append(self.names[i])
        if res != []:
            return res
        else:
            return ["nothing"]