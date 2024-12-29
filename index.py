"""
Author:Lorren
Time  : 2022年8月28日10:41:49
Function:Crawl the blog post of blogger csdn and save it in html/pdf/markdown formats
"""
import requests
import parsel
import os
import re
import html2text

def change_title(name):
    mode = re.compile(r'[\\\/\:\*\?\"\<\>\|]')
    newname = re.sub(mode, '_', name)
    return newname


filename = 'html\\'
filename2 = 'md\\'
if not os.path.exists(filename):
    os.mkdir(filename)

if not os.path.exists(filename2):
    os.mkdir(filename2)

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
{article}
</body>
</html>
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
# 假设你的长串cookie值存在变量cookie_str中
cookie_str = "uuid_tt_dd=10_30271976190-1731845821118-405417; fid=20_78750844239-1731845821719-877881; c_segment=9; hide_login=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1731845823; dc_session_id=10_1731848170288.507025; creative_btn_mp=3; HMACCOUNT=2ADD67F325DF81D0; SESSION=d51efff3-c1a4-42f6-a863-5add672b3667; c_hasSub=true; loginbox_strategy=%7B%22taskId%22%3A349%2C%22abCheckTime%22%3A1731845822747%2C%22version%22%3A%22exp11%22%2C%22blog-threeH-dialog-exp11tipShowTimes%22%3A8%2C%22blog-threeH-dialog-exp11%22%3A1731848170752%7D; popPageViewTimes=8; UserName=qq_39954083; UserInfo=678e65aa2352423f9972c3c4fc3ac824; UserToken=678e65aa2352423f9972c3c4fc3ac824; UserNick=%E5%91%A8%E7%BE%8E%E7%81%B5%E5%A4%A7%E5%A7%90%E5%A4%A7; AU=9C3; UN=qq_39954083; BT=1731849788221; p_uid=U010000; csdn_newcert_qq_39954083=1; dc_sid=7cb860133f59fd57890c5b2a3fe404fa; _clck=34bs1y%7C2%7Cfqy%7C0%7C1782; __gads=ID=a5b81df1bca357fb:T=1731848172:RT=1731850880:S=ALNI_MZql0OVVysfjPT7xMyX6ELUnvljGg; __gpi=UID=00000f975170b080:T=1731848172:RT=1731850880:S=ALNI_MZerW8ULRymrNfrO7wZFY_nRbLMOA; __eoi=ID=a03837f5c5db4f69:T=1731848172:RT=1731850880:S=AA-AfjZ7QfmfrH9xgji8tv0zDyKh; historyList-new=%5B%5D; fe_request_id=1731852940834_2348_7739471; c_utm_relevant_index=5; relevant_index=5; c_utm_medium=distribute.pc_search_result.none-task-chatgpt-2%7Eall%7Einsert_commercial%7Edefault-3-206a9898ee8e11ed9e3dfa163eeb3507-null-null.142%5Ev100%5Epc_search_result_base5; c_utm_term=python%E8%8E%B7%E5%8F%96csdn%E4%BB%98%E8%B4%B9%E4%B8%93%E6%A0%8F%E6%96%87%E7%AB%A0%E7%9A%84%E5%86%85%E5%AE%B9; _clsk=1mu0yo2%7C1731852959128%7C3%7C0%7Cz.clarity.ms%2Fcollect; log_Id_click=61; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/banxia_frontend/category_12225173_1.html; c_dsid=11_1731855338175.407103; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20231011044944.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Atrue%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%22qq_39954083%22%7D; c_pref=https%3A//blog.csdn.net/banxia_frontend/category_12225173_1.html; c_ref=https%3A//blog.csdn.net/banxia_frontend/category_12225173_20.html; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1731855408; c_page_id=default; dc_tos=sn3o6z; log_Id_pv=55; log_Id_view=1323"


# 将长串cookie解析成字典
cookies_dict = {}
for cookie in cookie_str.split(";"):
    parts = cookie.split("=")
    if len(parts) == 2:
        key, value = parts
        cookies_dict[key] = value
    else:
        print(f"跳过无效的cookie项: {cookie}")


# url = f'https://blog.csdn.net/banxia_frontend/category_12225173.html'
# # 此处替换相应想爬取的网址
# response = requests.get(url=url, headers=headers, cookies=cookies_dict)
# selector = parsel.Selector(response.text)
# href = selector.css(
#     '.column_article_list li a::attr(href)').getall()

# 基础的URL，用于后续拼接动态参数
# base_url = 'https://blog.csdn.net/banxia_frontend/category_12225173'
base_url = "https://blog.csdn.net/banxia_frontend/category_12436481"

# 用于存储所有请求得到的href结果
all_href = []

# 假设要循环请求的次数，可根据实际需求调整
num_requests = 1

for index in range(num_requests):
    # 动态生成带有索引参数的URL
    url = f'{base_url}_{index}.html'

    response = requests.get(url=url, headers=headers, cookies=cookies_dict)
    selector = parsel.Selector(response.text)
    href_list = selector.css('.column_article_list li a::attr(href)').getall()
    all_href.extend(href_list)

# 此处换成对应网页的对应属性即可
for i in all_href:
    response_1 = requests.get(url=i, headers=headers, cookies=cookies_dict)
    selector_1 = parsel.Selector(response_1.text)
    title = selector_1.css('#articleContentId::text').get()  # 文章标题的id
    newtitle = change_title(title)
    content_views = selector_1.css(
        '#content_views').get()  # 文章内容的id
    html_content = html_str.format(article=content_views)
    html_name = filename+newtitle+'.html'
    md_name = filename2 + newtitle+'.md'
    with open(html_name, mode='w', encoding='utf-8') as f:
        f.write(html_content)

    html_text = open(html_name, 'r', encoding='utf-8').read()
    markdown = html2text.html2text(html_text)
    with open(md_name, 'w', encoding='utf-8') as file:
        file.write(markdown)
        print("正在保存", newtitle, ".md")
