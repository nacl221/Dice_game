import tkinter as tk
import random

#変数の宣言
playnum=0 #遊んだ数
win=0  #勝った数
lose=0 #負けた数
draw=0 #引き分けの数
#ゲームの初期画面構成
root=tk.Tk() #ウィンドウオブジェクト作成
root.geometry("500x500") #ウィンドウの大きさ
canvas=tk.Canvas(root,width=500,height=500,bg="green") #背景の大きさと色
canvas.place(x=0,y=0) #背景の位置

#サイコロ画像をpythonで使えるようにする
dice1=tk.PhotoImage(file="images\\saikoro-illust1.png")
dice2=tk.PhotoImage(file="images\\saikoro-illust2.png")
dice3=tk.PhotoImage(file="images\\saikoro-illust3.png")
dice4=tk.PhotoImage(file="images\\saikoro-illust4.png")
dice5=tk.PhotoImage(file="images\\saikoro-illust5.png")
dice6=tk.PhotoImage(file="images\\saikoro-illust6.png")

#tkinter内のtext設定
TitleArea=tk.Label(text="賽の目比べ",font=("",20),fg="black")
TitleArea.place(x=20,y=20)
RivalArea=tk.Label(text="CPU",font=("",20),fg="red")
RivalArea.place(x=400,y=20)
PlayerArea=tk.Label(text="あなた",font=("",20),fg="blue")
PlayerArea.place(x=20,y=425)
PlaynumArea=tk.Label(text="遊:"+str(playnum),font=("",20),fg="blue")
PlaynumArea.place(x=400,y=320)
WinArea=tk.Label(text="勝:"+str(win),font=("",20),fg="blue")
WinArea.place(x=400,y=350)
LoseArea=tk.Label(text="負:"+str(lose),font=("",20),fg="blue")
LoseArea.place(x=400,y=380)
DrawArea=tk.Label(text="引:"+str(draw),font=("",20),fg="blue")
DrawArea.place(x=400,y=410)
Text=tk.Label(root,text="Let's duel!")
Text.place(x=400,y=220)
WinPar=tk.Label(text="率:0%",font=("",20),fg="blue")
WinPar.place(x=400,y=290)

#ボタンを押したとき何をするか
def click_button():
    RivalDice=random.randint(1,6)
    PlayerDice=random.randint(1,6) #両方のダイスを振る
    
    #Diceの数字とサイコロ画像を繋げ、画像をどこに置くかの設定
    if RivalDice==1:
        canvas.create_image(250,100,image=dice1)
    if RivalDice==2:
        canvas.create_image(250,100,image=dice2)
    if RivalDice==3:
        canvas.create_image(250,100,image=dice3)
    if RivalDice==4:
        canvas.create_image(250,100,image=dice4)
    if RivalDice==5:
        canvas.create_image(250,100,image=dice5)
    if RivalDice==6:
        canvas.create_image(250,100,image=dice6)
    if PlayerDice==1:
        canvas.create_image(250,400,image=dice1)
    if PlayerDice==2:
        canvas.create_image(250,400,image=dice2)
    if PlayerDice==3:
        canvas.create_image(250,400,image=dice3)
    if PlayerDice==4:
        canvas.create_image(250,400,image=dice4)
    if PlayerDice==5:
        canvas.create_image(250,400,image=dice5)
    if PlayerDice==6:
        canvas.create_image(250,400,image=dice6)

    #二つのサイコロの数を比べて勝敗をつける
    global playnum,win,lose,draw #グローバル宣言
    if PlayerDice>RivalDice:
        Text["text"]="You  win!"
        win+=1
        WinArea.configure(text="勝:"+str(win),font=("",20),fg="blue")
    if PlayerDice<RivalDice:
        Text["text"]="You lose..."
        lose+=1
        LoseArea.configure(text="負:"+str(lose),font=("",20),fg="blue")
    if PlayerDice==RivalDice:
        Text["text"]="draw"
        draw+=1
        DrawArea.configure(text="引:"+str(draw),font=("",20),fg="blue")
    playnum+=1
    PlaynumArea.configure(text="遊:"+str(playnum),font=("",20),fg="blue")
    WP=win/playnum*100
    WinPar.configure(text="率:"+str(round(WP))+"%",font=("",20),fg="blue")

    #ボタン設定
btn=tk.Button(root,text="サイコロを振る",command=click_button) #ボタンの文字となにを起こさせるかの設定
btn.place(x=220,y=220)  #ボタンの場所

