import gevent
from gevent import monkey
import time
import urllib.request

monkey.patch_all()


def downloader(image_name, image_url):
    req = urllib.request.urlopen(image_url)
    with open(image_name, "wb") as f:
        f.write(req.read())


def main():
    image_urls = [
        "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2574551676.webp",
        "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2575135153.webp",
        "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2573691764.webp",
        "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572847101.webp"
    ]

    gs = list()
    idx = 0
    for image_url in image_urls:
        idx += 1
        gs.append(gevent.spawn(downloader, str(idx) + ".webp", image_url))
    gevent.joinall(gs)


if __name__ == '__main__':
    main()
