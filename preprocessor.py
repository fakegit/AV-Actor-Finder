from image_crawler import ImageCrawler
from crop_face import FaceDetector

if __name__ == '__main__':
    print("#### Crawling the images ####")
    print("Enter the keywords : ")
    print("Example : 'sun, polar bear, moon'")
    keywords = input(">>")
    limit = int(input("Enter the limits >>"))

    crawler = ImageCrawler()
    crawler.crawl_images(keywords=keywords, limit=limit)
    print("#### Crawling Done ####")

    print("#### Cropping the faces ####")
    srcdir = input("Source directory >> ")
    desdir = input("Destination directory >> ")
    maxnum = int(input("Max number of samples per class >> "))

    detector = FaceDetector()

    detector.crop_faces_rootdir(srcdir, desdir, maxnum)
    print("#### Cropping Done ####")