import requests, time, multiprocessing
from bs4 import BeautifulSoup
import multiprocessing.pool


base = "https://www.projecteuler.net/"
problem = "problem"

# number due to 
# https://www.projecteuler.net/archives
start = 1
end = 672

def crawl(i):
    time.sleep(1)
    url = f"{base}{problem}={i}"
    page = requests.get(url)
    print(f"Crawling page {i} ....")
    time.sleep(1)
    soup = BeautifulSoup(page.text,"html.parser")
    content = soup.find("div",{"class":"problem_content"}).get_text().strip()
    with open(f"problems/problem{i}.md","w",encoding = "utf-8") as f:
        f.write(f"## Problem {i} of Euler Project \n")
        f.write(url+"\n")
        f.write(content)


if __name__ == "__main__":
    print("start crawlling ........")
    # for i in range(start,end+1):
    #     page = requests.get(f"{base}{problem}={i}")
    #     print(f"Crawling page {i} ....")
    #     time.sleep(1)
    #     soup = BeautifulSoup(page.text,"html.parser")
    #     content = soup.find("div",{"class":"problem_content"}).get_text().strip()
    #     with open(f"problems/problem{i}.md","w",encoding = "utf-8") as f:
    #         f.write(f"## Problem {i} of Euler Project \n")
    #         f.write(content)
    #     print(f"Page {i} DONE.")
    with multiprocessing.pool.ThreadPool() as executor:
        executor.map(crawl,[i for i in range(start,end +1)])

    print("All jobs DONE!")
            
