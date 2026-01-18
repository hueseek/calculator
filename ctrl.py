# ch 5.2.1 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    # calculate 메서드 추가. 내용은 추후에 작성
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.calculate) # 버튼 1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage)
