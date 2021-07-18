from youtubesearchpython import Video,Playlist,ResultMode

# video = Video.getInfo(("https://www.youtube.com/watch?v=9aW-knzZ7p8"))

# print(video["id"])
# print(video["title"])
# print(video["viewCount"]["text"])
# print(video["averageRating"])
# print(video["publishDate"])


# playlist_info = Playlist.getInfo("https://www.youtube.com/playlist?list=PLu0W_9lII9ahOwlLGfKljH86ni_muVoi7")
# playlist_video_info = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9ahOwlLGfKljH86ni_muVoi7")
# All_videos = eval(playlist_video_info.videos)

# for video in playlist_video_info.videos:
#     print(video['id'])

# print(playlist_info["videoCount"])
# print(playlist_info["viewCount"])


# VIDEO = playlist_video_info.videos
# for i in range(10):
#     print(VIDEO[i]["title"])
#     print(VIDEO[i]["thumbnails"][3]['url'])
#     print("\n----------------\n")
# playlist_info = Playlist.getInfo("https://www.youtube.com/playlist?list=PLu0W_9lII9ahOwlLGfKljH86ni_muVoi7")
# playlist_video_info = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9ahOwlLGfKljH86ni_muVoi7")
# tutorial = {}
# video_thumbnails = []
# video_titles = []
# tutorial['total_video'] = playlist_info["videoCount"]
# tutorial['views'] = playlist_info["viewCount"]
# VIDEO = playlist_video_info.videos
# for i in range(len(VIDEO)):
#     video_titles.append(VIDEO[i]["title"])
#     video_info = Video.getInfo(VIDEO['link'])
#     video_thumbnails.append(video_info["thumbnails"][3]['url'])     

# print(video_thumbnails)


# https://i9.ytimg.com/vi/hOF_hqB8b_Y/maxresdefault.jpg?time=1623831900000&sqp=CNzqpoYG&rs=AOn4CLCzlMYCmDUVEOH_QY14rQxPhkFCkg
# https://i9.ytimg.com/vi/oQY0xw25H98/maxresdefault.jpg?time=1623831900000&sqp=CNzqpoYG&rs=AOn4CLAg_wTCOQKMiw5cNTBzT9nHd0ThwA


# playlist = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

# while playlist.hasMoreVideos:
#     print('Getting more videos...')
#     playlist.getNextVideos()
#     # print(f'Videos Retrieved: {len(playlist.videos)}')
#     i = 1
# for v in playlist.videos:
#     print(i,". ",v["id"])
#     i+=1
# print("---------------------------------------------------------------")
# # else:


# from pytube import Channel

# ch = Channel("https://www.youtube.com/c/CodeWithHarry")
# count =1
# for v in ch.videos:
#     Scrap_video = Video.getInfo("https://www.youtube.com/watch?v="+v.video_id)
#     print(f'{count}) {Scrap_video["viewCount"]["text"]} ===== {Scrap_video["title"]}')
#     count+=1
import json

Config = None
with open("config.json","r") as f:
    Config = json.loads(f.read())
print(type(Config))
print(Config["paras"]["api_key"])
