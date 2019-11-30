import sys
from tkinter import messagebox, Toplevel, Label, Button, Tk

'''
    Name：人机对战井字棋
    Author：Tom Guo
    Version:1.0.3
'''

class wel:
    def __init__(self, win):
        self.win=win
        self.win1 = Toplevel(win)  # 子窗口
        self.win1.geometry("640x640+650+200")
        self.welTitle = Label(self.win1, text="欢迎来玩井字棋游戏！", font='微软雅黑 -34 bold', fg='red')
        self.welTitle.place(x=160, y=20)
        self.chTitle = Label(self.win1, text="请选择先手方：", font='宋体 -24 bold', fg='black')
        self.chTitle.place(x=50, y=120)
        self.b1 = Button(self.win1, text='玩 家 先', width=14, height=3, font='微软雅黑 -24 bold', bg='white',
                         activebackground='grey', bd=4,
                         command=self.playerTurn)
        self.b1.place(x=200, y=200)
        self.b2 = Button(self.win1, text='电 脑 先', width=14, height=3, font='微软雅黑 -24 bold', bg='white',
                         activebackground='grey', bd=4,
                         command=self.pcTurn)
        self.b2.place(x=200, y=400)

    def pcTurn(self):  # 电脑先手
        turn = 'pc'
        firTurn = turn
        self.win1.state('iconic')
        self.newPlay = play(self.win, turn, firTurn,self.win1)
        self.newPlay.pcGo()

    def playerTurn(self):  # 玩家先手
        turn = 'player'
        firTurn = turn
        self.win1.state('iconic')
        self.newPlay = play(self.win, turn, firTurn,self.win1)


class play(wel):
    def __init__(self, win, turn, firTurn,win1):
        self.win1=win1
        self.win = win
        self.turn = turn
        self.firTurn = firTurn  # 先手者
        self.winner = ''  # 获胜者
        self.WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # 所有获胜方法
        self.BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)  # 最佳下棋位置表
        self.win2 = Toplevel(self.win)  # 子窗口
        self.win2.geometry("640x640+650+200")
        self.l0 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')  # 九个格子
        self.l0.place(x=100, y=80)
        self.l1 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l1.place(x=240, y=80)
        self.l2 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l2.place(x=380, y=80)
        self.l3 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l3.place(x=100, y=235)
        self.l4 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l4.place(x=240, y=235)
        self.l5 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l5.place(x=380, y=235)
        self.l6 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l6.place(x=100, y=390)
        self.l7 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l7.place(x=240, y=390)
        self.l8 = Label(self.win2, text='    ', font='微软雅黑 -100 bold', fg='red', bg='white')
        self.l8.place(x=380, y=390)
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 创建新逻辑棋盘
        self.l0.bind("<Button-1>", self.touch0)  # 绑定按钮事件
        self.l1.bind("<Button-1>", self.touch1)
        self.l2.bind("<Button-1>", self.touch2)
        self.l3.bind("<Button-1>", self.touch3)
        self.l4.bind("<Button-1>", self.touch4)
        self.l5.bind("<Button-1>", self.touch5)
        self.l6.bind("<Button-1>", self.touch6)
        self.l7.bind("<Button-1>", self.touch7)
        self.l8.bind("<Button-1>", self.touch8)
        self.win2.bind_all("<Button-1>", self.result)

    # 九个格子对应的事件
    def touch0(self, event):
        if self.board[0] == 0:
            if self.firTurn == 'pc':
                self.l0['text'] = " O "
            else:
                self.l0['text'] = " X "
            self.board[0] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch1(self, event):
        if self.board[1] == 0:
            if self.firTurn == 'pc':
                self.l1['text'] = " O "
            else:
                self.l1['text'] = " X "
            self.board[1] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch2(self, event):
        if self.board[2] == 0:
            if self.firTurn == 'pc':
                self.l2['text'] = " O "
            else:
                self.l2['text'] = " X "
            self.board[2] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch3(self, event):
        if self.board[3] == 0:
            if self.firTurn == 'pc':
                self.l3['text'] = " O "
            else:
                self.l3['text'] = " X "
            self.board[3] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch4(self, event):
        if self.board[4] == 0:
            if self.firTurn == 'pc':
                self.l4['text'] = " O "
            else:
                self.l4['text'] = " X "
            self.board[4] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch5(self, event):
        if self.board[5] == 0:
            if self.firTurn == 'pc':
                self.l5['text'] = " O "
            else:
                self.l5['text'] = " X "
            self.board[5] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch6(self, event):
        if self.board[6] == 0:
            if self.firTurn == 'pc':
                self.l6['text'] = " O "
            else:
                self.l6['text'] = " X "
            self.board[6] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch7(self,event):
        if self.board[7] == 0:
            if self.firTurn == 'pc':
                self.l7['text'] = " O "
            else:
                self.l7['text'] = " X "
            self.board[7] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def touch8(self, event):
        if self.board[8] == 0:
            if self.firTurn == 'pc':
                self.l8['text'] = " O "
            else:
                self.l8['text'] = " X "
            self.board[8] = 1  # 设置逻辑棋盘
            self.pcGo()
        else:
            messagebox.showwarning('错误', '此处已落子！')

    def judge(self):  # 判断胜负函数
        for row in self.WAYS_TO_WIN:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != 0:
                if self.board[row[0]] == 1:
                    self.winner = 'player'
                if self.board[row[0]] == -1:
                    self.winner = 'pc'

    def result(self,event):  # 结局提示函数
        for row in self.WAYS_TO_WIN:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != 0:
                if self.board[row[0]] == 1:
                    messagebox.showinfo('胜利', '恭喜你，玩家获胜！')
                else:
                    messagebox.showinfo('失败', '真可惜，电脑获胜...')
                ask = messagebox.askquestion('询问', '是否再下一局？')
                if ask == 'yes':
                    self.win2.destroy()
                    self.board=[0,0,0,0,0,0,0,0,0]
                    self.win1.state('normal')
                else:
                    sys.exit()
        if 0 not in self.board:
            messagebox.showinfo('提示', '平局！')
            ask = messagebox.askquestion('询问', '是否再下一局？')
            if ask == 'yes':
                self.win2.destroy()
                self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.win1.state('normal')
            else:
                sys.exit()

    def pcGo(self):  # 电脑走棋
        self.emptyLoc = []
        self.list = (self.l0, self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8)
        for i in range(9):
            if self.board[i] == 0:
                self.emptyLoc.append(i)
        # 如果电脑能赢，就走那个位置
        for move in self.emptyLoc:
            self.board[move] = -1
            self.judge
            if self.winner == 'pc':
                temp = 0
                for i in self.list:
                    if temp == move:
                        if self.firTurn == 'pc':
                            i['text'] = " X "
                        else:
                            i['text'] = " O "
                        return
                    else:
                        temp = temp + 1
            # 取消走棋方案
            self.board[move] = 0
        # 如果玩家能赢，就堵住那个位置
        for move in self.emptyLoc:
            self.board[move] = 1
            self.judge
            if self.winner == 'player':
                temp = 0
                self.board[move] = -1
                for i in self.list:
                    if temp == move:
                        if self.firTurn == 'pc':
                            i['text'] = " X "
                        else:
                            i['text'] = " O "
                        return
                    else:
                        temp = temp + 1
            # 取消走棋方案
            self.board[move] = 0
        # 不是上面情况则也就是这一轮时都赢不了，则从最佳下棋位置表中挑出第一个合法位置
        for move in self.BEST_MOVES:
            if move in self.emptyLoc:
                temp = 0
                self.board[move] = -1
                for i in self.list:
                    if temp == move:
                        if self.firTurn == 'pc':
                            i['text'] = " X "
                        else:
                            i['text'] = " O "
                        return
                    else:
                        temp = temp + 1


class main:
    def __init__(self, root):
        self.mainWindow = root
        self.mainWindow.geometry("640x640+650+200")  # 设置大小
        self.mainWindow.title("人机对战井字棋")
        self.mainWindow.state('iconic')  # 最小化底层窗口
        wel(self.mainWindow)


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.mainloop()
