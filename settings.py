class Buttons():
    #返回按钮
    tapreturn_x = 100
    tapreturn_y = 45

    #凭证交易按钮
    pzjy_x = 933
    pzjy_y = 120

    # #主页商店按钮
    # shop_x = 938
    # shop_y = 538

    def __init__(self):

        #点击挑战范围
        self.start_x = [1402, 1578]
        self.start_y = [710, 779]
        #结束点击范围
        self.end_x = [850, 1139]
        self.end_y = [677, 899]
        #进入商店按钮
        self.shop_x = [860, 1013]
        self.shop_y = [490, 584]
        #进入基建按钮
        self.base_x = [1139, 1188]
        self.base_y = [633, 768]
        #进入公招按钮
        self.employ_x = [1053, 1198]
        self.employ_y = [536, 605]
        #进入任务按钮
        self.task_x = [811, 1003]
        self.task_y = [633, 714]

        #主页gear位置
        self.gear_x = [17, 71]
        self.gear_y = [26, 81]

        #credict_position
        self.cred_x = [1299, 1356]
        self.cred_y = [30, 56]


class ShopButtons():

    #商店十个坐标
    def __init__(s):

        s.x1 = [60, 240]
        s.y1 = [166, 205]

        s.x2 = [350, 530]
        s.y2 = [166, 205]

        s.x3 = [630, 810]
        s.y3 = [166, 205]

        s.x4 = [920, 1100]
        s.y4 = [166, 205]

        s.x5 = [1200, 1380]
        s.y5 = [166, 205]

        s.x6 = [66, 240]
        s.y6 = [451, 490]

        s.x7 = [350, 530]
        s.y7 = [451, 490]

        s.x8 = [626, 814]
        s.y8 = [451, 490]

        s.x9 = [916, 1100]
        s.y9 = [451, 490]

        s.x10 = [1199, 1385]
        s.y10 = [451, 490]

        s.shoptag = [[s.x1, s.y1], [s.x2, s.y2], [s.x3, s.y3], [s.x4, s.y4], [s.x5, s.y5],\
                  [s.x6, s.y6], [s.x7, s.y7], [s.x8, s.y8], [s.x9, s.y9], [s.x10, s.y10]]

        s.buylist=['技巧概要·卷2', '技巧概要·卷1', '中级作战记录', '初级作战记录', '基础作战记录', '招聘许可']

