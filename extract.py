""" Test of the pytube extract functionality """
from pytube import YouTube, Search


def get_yt_audio(link):
    yt = YouTube(link)
    stream=yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
    path=stream.download()
    return path


def get_urls(search_term):
    url_dict = {}
    s = Search(search_term)
    for key, obj in enumerate(s.results):
        url_dict[key] = {'title': obj.title,
                         'url': obj.watch_url,
                         'thumbnail_url': obj.thumbnail_url}
        #print(f"{obj.title} {obj.watch_url} {obj.thumbnail_url}")

    return url_dict

if __name__ == '__main__':
    url_dict = get_urls('Suede generation')
    for key, value in url_dict.items():
        print(key, value)
    choice = -1
    print(url_dict.keys())
    while choice not in url_dict.keys():
        choice = int(input("Please select a number: "))
    link = url_dict[choice]['url']
    print(f"link {type(link)}")
    file = get_yt_audio(link)
    print(file)