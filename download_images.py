from google_images_download import google_images_download
from argparse import ArgumentParser

def download(query, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": query, "limit": limit, "print_urls": False}
    paths = response.download(arguments)

if __name__ == "__main__":
    parser = ArgumentParser(description="Downloads an image dataset.")
    parser.add_argument("limit", metavar="N", type=int, help="The max number of images per class (no more than 100 per class)")
    parser.add_argument("queries", metavar="Q", type=str, nargs="+", help="Query terms, e.g. dogs cats")
    args = parser.parse_args()
    for query in args.queries:
        download(query, args.limit)

