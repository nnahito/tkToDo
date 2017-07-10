#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import Tkinter
import sqlite3

# Database名
dbname = 'todolist.db'

# Databaseに接続
conn = sqlite3.connect(dbname)
c = conn.cursor()

# 未完予定リストを全件取得
sql = 'select id, content, flag from todo where flag = 0'
allList = c.execute(sql)



#
# Tkinterの準備ここから
#
root = Tkinter.Tk()
root.title(u"tk ToDo")
root.geometry("300x400")


#
# 予定追加ボタンが押されたときの処理定義
#

def addToDoList(event):
    # EditBoxからデータを取得
    task = addToDoBox.get()

    if ( task == '' ):
        return None

    # SQL文準備
    sql = 'insert into todo (content, flag) values ("'+ task +'", 0)';

    # Databaseに追加
    c.execute(sql)
    conn.commit()

    # ListBoxにも追加
    todoListBox.insert(Tkinter.END, task)

    # ToDo入力ボックスを空に
    addToDoBox.delete(0, Tkinter.END)




#
# ToDo完了ボタンが押されたときの処理定義
#
def completeToDo(event):
    # 選択されているリストの番号
    selectedIndex = Tkinter.ACTIVE

    # そいつを削除
    todoListBox.delete(selectedIndex)

    # テキストを取得（だめだけど時間ないからこいつをキーにする(´；ω；｀)）
    todoText = todoListBox.get(selectedIndex)

    # Databaseのフラグをおる
    sql = 'update todo set flag = 1 where content = "'+ todoText +'" '

    # Database編集
    c.execute(sql)
    conn.commit()





#
# Tkinterに表示するウィジェットの定義
#

# エントリー（予定入力用）
addToDoBox = Tkinter.Entry()
addToDoBox.pack()

# 予定追加ボタン
addToDoButton = Tkinter.Button(text=u'ToDo追加')
addToDoButton.bind("<Button-1>", addToDoList)
addToDoButton.pack()


# リストボックス（未完予定用）
todoListBox = Tkinter.Listbox(width=30, height=18)
todoListBox.pack()


# 予定完了ボタン
completeToDoButton = Tkinter.Button(text=u'ToDo完了')
completeToDoButton.bind("<Button-1>", completeToDo)
completeToDoButton.pack()








# リストボックスに、未完リストを表示する
for row in allList:
    if ( row != '' ):
        todoListBox.insert(Tkinter.END, row[1])




root.mainloop()
