from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from requests.sessions import session
import random,smtplib
import random,datetime,sys,time
from youtubesearchpython import Playlist
import json
from tutorials_info import Tutorials_info
from googleapiclient.discovery import build

app = Flask(__name__,template_folder="templats")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/programminglearner'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

# config.json
Paras = None
with open("config.json","r") as f:
    Paras = json.loads(f.read())["paras"]

# Globle varialbles
Video_name_id = {}
all_videos = []
Recently_video = []
top_10_videos = []
populer_tutorials = []
recently_tutorial = []
global_result = None

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_num = request.form['phone_num']
        message = request.form['message']
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(Paras["email_address"],Paras["email_password"])
            Message = f'''
                Name : {first_name} {last_name}
                Email : {email}
                Pjone num. : {phone_num}
                -----------------------------
                Message : {message}
                '''
            mail = f"Subject: Contact me !! Programming Learner \n\n {Message}"
            
            s.sendmail(Paras["email_address"], "manearyan4321@gmail.com" , mail)
            s.quit()
            return render_template("index.html",contact_success=True)
        except:
            return "<h1>Something went wroung.... Try again !! </h1>"

    return render_template("index.html")
    
@app.route("/tutorials")
def tutorials():
    global populer_tutorials,recently_tutorial

    for tutorial in Tutorials_info:
        if "static/img" not in tutorial["thumbnail"]:
            tutorial["thumbnail"] = url_for('static', filename=f"img/{tutorial['thumbnail']}")

    if populer_tutorials == [] and recently_tutorial == []:
        all_tutorial_views = []
        for tutorial in Tutorials_info:
            try:
                tutorial["views"] = Playlist.getInfo(tutorial["url"])["viewCount"]
            except:
                return "<h1>Somthing went wroung....</h1>"
            tutorial["redirect"] = "/tutorials/"+str(tutorial['name']).replace("#"," ").replace(" ","+")
            tutorial["int_views"] = int(str(tutorial["views"]).split(" views")[0].replace(",",""))
            all_tutorial_views.append(tutorial["int_views"])
        # Populer
        all_tutorial_views.sort(reverse=True)
        count = 0
        for views in all_tutorial_views:
            for tutorial in Tutorials_info:
                if tutorial["int_views"] == views:
                    populer_tutorials.append(tutorial)
                    count+=1
                    if count == 6:
                        break
        # recently
        try:
            recently_tutorial.append(Tutorials_info[-3])
            recently_tutorial.append(Tutorials_info[-2])
            recently_tutorial.append(Tutorials_info[-1])
        except:
            try:
                recently_tutorial.append(Tutorials_info[-2])
                recently_tutorial.append(Tutorials_info[-1])
            except:
               recently_tutorial.append(Tutorials_info[0])
          
    all_tutorials = Tutorials_info
    all_tutorials.reverse()

    return render_template("tutorials.html",recently_tutorial=recently_tutorial,populer_tutorials=populer_tutorials,len=len,all_tutorial=all_tutorials)

@app.route("/tutorials/<string:tutorial_name>",methods=["GET","POST"])
def tutorial_content(tutorial_name):
    tutorial = []

    for tut in Tutorials_info:
        if str(tut["name"]).replace("#"," ").replace(" ","+") == tutorial_name:
            tutorial = tut
            if "static/img" not in tutorial["thumbnail"]:
                tutorial["thumbnail"] = url_for('static', filename=f"img/{tutorial['thumbnail']}")


               
    tutorial['total_video'] = len(tutorial["videos"])
    
    return render_template("tutorial-content.html",tutorial=tutorial,len=len)

@app.route("/video/<video_id>",methods=["GET","POST"])
def video_content(video_id):
    is_tutorial = False
    
    #Check if video in tutorial
    for tut in Tutorials_info:
        for i in range(len(tut["videos"])):
            if tut["videos"][i]["id"] == video_id:
                is_tutorial = True
                break

    next_video_id = ""
    pre_video_id = ""

    # video in tutorial
    if is_tutorial:
        Video_info = {}
        tutorial_url = ""
        for tut in Tutorials_info:
            for i in range(len(tut["videos"])):
                if tut["videos"][i]["id"] == video_id:
                    Video_info = tut["videos"][i]
                    tutorial_url =  "/tutorials/"+str(tut['name']).replace("#"," ").replace(" ","+")

                    try:
                        if i != 0:
                            pre_video_id = tut["videos"][i-1]["id"]
                        else:
                            pre_video_id = "No"
                    except:
                        pre_video_id = "No"
                    try:
                        next_video_id = tut["videos"][i+1]["id"]
                    except:
                        next_video_id = "No"

                    # Reading code file
                    if Video_info["code"]["file"]:
                        Video_info["code"]["full_code"] = []
                        for i in range(len(Video_info["code"]["file_name"])):
                            with open(f'static/code/{Video_info["code"]["file_name"][i]}',"r") as f:
                                Video_info["code"]["full_code"].append(f.read())
                  
                    return render_template("video_content.html",is_tutorial=is_tutorial,pre_video_id=pre_video_id,next_video_id=next_video_id,Video_info=Video_info,len=len,tutorial_url=tutorial_url)
    
    return "<h1>Url is incorrect....</h1>"

    # normal video
    # else:

    #     return render_template("video_content.html",normal_video=True,len=len)

# @app.route("/videos")
# def videos():
#     global all_videos,Recently_video,top_10_videos

#     if len(all_videos) == 0 and len(Recently_video) == 0 and len(top_10_videos) == 0:
#         for tut in Tutorials_info:
#             for video in tut["videos"]:
#                 all_videos.append(video)
#         # Populer
        
#         api_key = Paras["api_key"]
#         youtube = build('youtube', 'v3', developerKey=api_key)
#         playlist_id = Paras["All_videos_playlist"].split("playlist?list=")[1]
#         videos = []
#         nextPageToken = None

#         while True:
#             pl_request = youtube.playlistItems().list(
#                 part='contentDetails',
#                 playlistId=playlist_id,
#                 maxResults=50,
#                 pageToken=nextPageToken
#             )

#             pl_response = pl_request.execute()

#             vid_ids = []
#             for item in pl_response['items']:
#                 vid_ids.append(item['contentDetails']['videoId'])

#             vid_request = youtube.videos().list(
#                 part="statistics",
#                 id=','.join(vid_ids)
#             )

#             vid_response = vid_request.execute()

#             for item in vid_response['items']:
#                 vid_views = item['statistics']['viewCount']

#                 vid_id = item['id']
            
#                 videos.append(
#                     {
#                         'views': int(vid_views),
#                         'id': vid_id,
#                     }
#                 )

#             nextPageToken = pl_response.get('nextPageToken')

#             if not nextPageToken:
#                 break

#         videos.sort(key=lambda vid: vid['views'], reverse=True)

#         for video1 in videos[:10]:
#             for video2 in all_videos:
#                 if video1["id"] == video2["id"]:
#                     top_10_videos.append(video2)
#                     try:all_videos.remove(video2)
#                     except:pass

#         try:
#             Recently_video = all_videos[:4]
#             all_videos = all_videos[4:]
#         except:
#             Recently_video = all_videos[:3]
#             all_videos = all_videos[3:]
#     total_size = 0
#     for video in top_10_videos:
#         total_size+=sys.getsizeof(video)
   
   
#     return render_template("videos.html",all_videos=all_videos,Recently_video=Recently_video,top_10_videos=top_10_videos)

@app.route("/contact")
def contact():
   
    return render_template("contact.html")

@app.route("/projects",methods=["POST","GET"])
def projects():
    project_videos = []
    for tut in Tutorials_info:
        try:
            if tut["is_project_playlist"]:
                for v in tut["videos"]:
                    project_videos.append(v)
        except:
            for video in tut["videos"]:
                try:
                    if video["is_project"]:
                        project_videos.append(video)
                except:pass

    new_project_videos = []
    for i in range(len(project_videos)):
        rand_choice = random.choice(project_videos)
        new_project_videos.append(rand_choice)
        project_videos.remove(rand_choice)

    return render_template("projects.html",all_project_videos=new_project_videos)

@app.route("/search/<search>")
def search_result(search):
    global global_result
    time1 = time.time()
    search_query=str(search.replace("+"," "))
    result = []
    try_result = False

    for tut in Tutorials_info:
        if search_query.lower() in str(tut["name"]).lower():
            tut["type"] = "tutorial"
            if "static/img" not in tut["thumbnail"]:
                tut["thumbnail"] = url_for('static', filename=f"img/{tut['thumbnail']}")
            tut["redirect"] = "/tutorials/"+str(tut['name']).replace("#"," ").replace(" ","+")
            tut["count"] = str(tut["name"]).lower().count(search_query.lower())
            result.append(tut)
        elif search_query.lower() in str(tut["dsc"]).lower():
            tut["type"] = "tutorial"
            if "static/img" not in tut["thumbnail"]:
                tut["thumbnail"] = url_for('static', filename=f"img/{tut['thumbnail']}")
            tut["redirect"] = "/tutorials/"+str(tut['name']).replace("#"," ").replace(" ","+")
            tut["count"] = str(tut["name"]).lower().count(search_query.lower())
            result.insert(len(result),tut)

        for video in tut["videos"]:
            if search_query.lower() in str(video["title"]).lower():
                video["count"] = str(video["title"]).lower().count(search_query.lower())
                video["type"] = "video"
                if len(result) > 50:
                    break
                result.append(video)

            elif search_query.lower() in str(video["dsc"]):
                video["count"] = str(video["title"]).lower().count(search_query.lower())
                video["type"] = "video"
                if len(result) > 50:
                    break
                result.insert(len(result),video)

    # If result are 0
    if len(result) == 0:   
        for count in range(len(str(search_query).split(" "))):
            for tut in Tutorials_info:
                if search_query.lower().split(" ")[count] in str(tut["name"]).lower():
                    tut["type"] = "tutorial"
                    if "static/img" not in tut["thumbnail"]:
                        tut["thumbnail"] = url_for('static', filename=f"img/{tut['thumbnail']}")
                    tut["redirect"] = "/tutorials/"+str(tut['name']).replace("#"," ").replace(" ","+")
                    result.append(tut)
                elif search_query.lower().split(" ")[count] in str(tut["dsc"]).lower():
                    tut["type"] = "tutorial"
                    if "static/img" not in tut["thumbnail"]:
                        tut["thumbnail"] = url_for('static', filename=f"img/{tut['thumbnail']}")
                    tut["redirect"] = "/tutorials/"+str(tut['name']).replace("#"," ").replace(" ","+")
                    result.insert(len(result),tut)

                for video in tut["videos"]:
                    if search_query.lower().split(" ")[count] in str(video["title"]).lower():

                        video["type"] = "video"
                        result.append(video)
                    elif search_query.lower().split(" ")[count] in str(video["dsc"]):
                        video["type"] = "video"
                        result.insert(len(result),video)

        if len(result) == 0:
            try_result = True
            while 1:
                if len(result) == 5:break
                tutorial_random = random.choice([i for i in Tutorials_info])
                video_random = random.choice([i for i in tutorial_random["videos"]])
                video_random["type"] = "video"
                if video_random not in result:
                    result.append(video_random)
    else:
        for i in range(len(result)):
            for j in range(len(result)-1):
                if result[i]["count"] > result[j]["count"]:
                    result[i],result[j] = result[j],result[i]

    time2 = time.time()

    if try_result :
        result_title = f"About 0 results ({round(time2-time1,2)} seconds)"
    else:
        result_title = f"About  {len(result)} results ({round(time2-time1,2)} seconds)"
    global_result = result
    return render_template("search-result.html",search_query=search_query,result=result,len=len,result_title=result_title,try_result=try_result)

@app.route("/user_activities",methods=["GET","POST"])
def activities():
    all_videos = []
    for tut in Tutorials_info:
        for video in tut["videos"]:
            all_videos.append(video)
    return render_template("activities.html",all_videos=all_videos)
    
@app.route("/coming_soon")
def coming_soon():
    return render_template("coming_soon.html")
    

if __name__ == '__main__':
    
    app.run(debug=False)
