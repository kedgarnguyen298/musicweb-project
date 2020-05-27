import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# connect 
url = "https://www.nhaccuatui.com/bai-hat/top-20.au-my.html"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")

# f = open("zingchart.html", "wb")
# f.write(raw_data)
# f.close()

# Extra ROI
soup = BeautifulSoup(page_content, "html.parser")
list_chart_page = soup.find("div", "list_chart_page")
resource_slide = list_chart_page.find("div", "box_resource_slide")
list_chart_slide = resource_slide.ul

# Extra data
list_chart_info = [] 

list_chart = list_chart_slide.find_all("li")

for chart in list_chart:
    rank_field = chart.find("span", "chart_tw")
    rank = rank_field.string
    info_field = chart.find("div", "box_info_field")
    link = info_field.a["href"]
    title = info_field.h3.a.string
    singer_list_a = info_field.h4.find_all("a")
    singer_list = []
    for a in singer_list_a:
        singer = a.string
        singer_list.append(singer)

    chart_info = {
        "rank": rank,
        "title": title,
        "link": link,
        "singers": singer_list
    }
    
    list_chart_info.append(chart_info)

print(list_chart_info)

 
