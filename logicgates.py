# _*_ coding: utf-8 _*_
# @File Name: logicgates.py
# @Time: 2024/6/12 14:56
# @Author: Dongdong
# @E-mail Address: 1141305121@qq.com

# 定义最通用的逻辑类，与门、或门和非门都继承于此
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):

        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate"+self.getLabel()+"-->"))
    def getPinB(self):
        return int(input("Enter Pin B input for gate"+self.getLabel()+"-->"))

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

    def inputPin(self):
        if self.pinA is None:
            self.pinA = self.getPinA()
        if self.pinB is None:
            self.pinB = self.getPinB()

class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate"+self.getLabel()+"-->"))

    def setNextPin(self, source):
        if self.pin is None:
           self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    def inputPin(self):
        if self.pin is None:
            self.pin = self.getPin()

class AndGate(BinaryGate):  # 创建与门

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.pinA is None or self.pinB is None:
            raise RuntimeError("Error: NO EMPTY PINS")
        else:
            if (self.pinA == 1) and (self.pinB == 1):
                return int(1)
            else:
                return int(0)

class OrGate(BinaryGate):  # 创建或门

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.pinA is None or self.pinB is None:
            raise RuntimeError("Error: NO EMPTY PINS")
        else:
            if (self.pinA == 1) or (self.pinB == 1):
                return int(1)
            else:
                return int(0)

class NotGate(UnaryGate):  # 创建非门

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.pin is None:
            raise RuntimeError("Error: NO EMPTY PINS")
        else:
            if self.pin == 1:
                return int(0)
            else:
                return int(1)

class Connector:  # 创立连接类

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        fgate.inputPin()
        tgate.setNextPin(fgate.getOutput())

if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    C1 = Connector(g1, g3)
    C2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())
