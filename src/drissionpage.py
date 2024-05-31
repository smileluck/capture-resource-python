from DrissionPage import ChromiumPage
import time

if __name__ == "__main__":

    page = ChromiumPage()

    url = "https://pixabay.com/zh/videos/search/?order=ec&pagi=%s"

    page.get(url % "2")

    page.listen.start("https://pixabay.com/zh/videos/search/?order=ec")


    page.ele(".:pages").child().click()

    res = page.listen.wait()  # 等待并获取一个数据包
    print(res)

    for _ in range(5):

        ul_ele = page.ele("tag:span@@text():下一页").parent()
        ul_ele.click()  # 点击下一页

        res = page.listen.wait()  # 等待并获取一个数据包
        print(res)  # 打印数据包url

    time.sleep(100000)
