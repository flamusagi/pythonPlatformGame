
#创建关卡类
class Level():
    def __init__(self,level,max_levels):
        self.level=level
        self.max_levels=max_levels
    def setLevel(self,level,max_levels):
        self.level=level
        self.max_levels=max_levels
    def getLevel(self):
        return self.level
    def getMaxLevel(self):
        return self.max_levels

# 创建通关个数类
class Complete():
    def __init__(self,clear_num,all_clear):
        self.clear_num=clear_num
        self.all_clear=all_clear
    def setClear(self,clear_num):
        self.clear_num=clear_num
    def getClear(self):
        return self.clear_num
    def is_win(self):
        if self.clear_num==self.all_clear:
            return True
        else:
            return False
    def is_complete(self,play,index):
        if play[index]:
            return True
        else:
            return False
