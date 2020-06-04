from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from data import crawlData, getAllSong
from controller import formatName, getRecommendList
from model.main import Song

from mongoengine import *
connect(db='musicweb-database',
        username='admin',
        password='admin',
        )

import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-jzaci.mongodb.net/musicweb-database?retryWrites=true&w=majority")
db = client["musicweb-database"]
cl = db.song

list_song_info = getAllSong()


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    print(list_song_info)
    if request.method == "POST":
        title = request.form['search']
        for song_info in list_song_info:
            if song_info["title"] == title:
                idSong = song_info["id"]
                return redirect("/play/" + idSong)
            else:
                continue
    return render_template('home.html')

@app.route('/charts', methods = ["GET", "POST"])
def chart():
    list_chart_info = crawlData()
    if request.method == "POST":
        title = request.form['search']
        for song_info in list_song_info:
            if song_info["title"] == title:
                idSong = song_info["id"]
                return redirect("/play/" + idSong)
            else:
                continue
    return render_template('charts.html', list_chart_info = list_chart_info)

@app.route('/play/<idSong>', methods = ["GET", "POST"]) 
def play(idSong):
    # Find Singer
    # for info in list_chart_info:
    #     idInInfo = info["id"]
    #     if idSong == idInInfo:
    #         singer = info["singers"]
    #         singer = singer[0]

    # singer = formatName(singer)
    # list_recommend_info = dataBaseSinger(singer)
    list_chart_info = crawlData()
    if request.method == "POST":
        title = request.form['search']
        for song_info in list_song_info:
            if song_info["title"] == title:
                idSong = song_info["id"]
                return redirect("/play/" + idSong)
            else:
                continue
    recommendList = getRecommendList(list_chart_info)
    return render_template('running.html', idSong = idSong, recommendList=recommendList)

@app.route('/update')
def insert_song():
    list_song_info = getAllSong()
    cl.insert(list_song_info)
    return render_template("confirmUpdate.html", list_song_info=list_song_info)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 