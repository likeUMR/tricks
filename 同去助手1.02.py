#!/usr/bin/env python
# coding: utf-8

# In[1]:

# 需要安装requests库：pip install requests
import requests
import re
import json
import webbrowser
import time
import tkinter as tk

# In[2]:

#已废弃，见README
#仍具有参考价值（哭）
def start_whole_thing():
    # config
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
               'Cookie': 'UM_distinctid=1786c37bce19bf-03a966f2aabbda-5c3f1d4d-144000-1786c37bce2b73; Hm_lvt_fcd79bd95b6da3b03dfe6cbc0dd48b21=1617005043,1618214278,1619069887; tq_ci_session_id=n048l597g2ls53qf67j9sip51m35iqqb'}


    # 寻找“新时代社会认知实践”字样，可自行切换其他字样
    search_target = r"\\u65b0\\u65f6\\u4ee3\\u793e\\u4f1a\\u8ba4\\u77e5\\u5b9e\\u8df5"
    # 设置标记
    charIsShiJian = "*"
    charHaveEnrolled = "OK"
    charIsFull = "已满"
    charAvailable = "-->"
    charNotAvailable = "[未开]"

    url = "https://tongqu.sjtu.edu.cn/act/type?type=0&status=0&order=hotvalue"
    url2 = "https://tongqu.sjtu.edu.cn/act/type?type=0&status=0&order=sign_start_time"
    url_me = "https://tongqu.sjtu.edu.cn/user/act"
    website = r"https://tongqu.sjtu.edu.cn/act/"

    me_response = requests.get(url_me, headers=headers)
    print(me_response.text)
    res = re.search("var g_user_acts.*</script>", me_response.text)
    # print(res[0])
    # me_info = re.findall('{\"actid\".*?\"}', res[0])
    done_list = []

    # for me_sec in me_info:
    #     # print(me_sec)
    #     id_info = re.search(r'\"actid\":\".{5}', me_sec)
    #     done_list.append(id_info[0][-5:])

    response = requests.get(url2, headers=headers)
    res = re.search("var g_init_type_acts.*</script>", response.text)
    info = re.findall('{\"actid\".*?\"}', res[0])

    data_set = {}
    count = 0
    for sec in info:
        t_t = ""
        dict = json.loads(sec)
        pa = dict["member_count"]
        pb = dict["max_member"]

        act_url = f"https://tongqu.sjtu.edu.cn/act/{dict['actid']}"
        act_res = requests.get(act_url, headers=headers)

        if re.search(search_target, act_res.text):
            # print('*',end="")
            t_t = t_t+charIsShiJian

        if dict['actid'] in done_list:
            t_t = t_t+charHaveEnrolled+pa+'/'+pb+"   "
        elif pa == pb:
            #print("【已满】"+pa+'/'+pb,end="   ")
            t_t = t_t+charIsFull+pa+'/'+pb+"   "
        elif dict["time_status"] == 2:
            t_t = t_t+charNotAvailable+pa+'/'+pb+"   "
        else:
            #print("【OK】"+pa+'/'+pb,end="   ")
            t_t = t_t+charAvailable+pa+'/'+pb+"   "
        for j in ["name", "location", "start_time", "end_time"]:
            #print(dict[j],end=" ")
            t_t = t_t+dict[j]+" "
        # print('')
        data_set[t_t] = dict['actid']
        count = count+1
        if count > 2:
            break

    response = requests.get(url, headers=headers)
    res = re.search("var g_init_type_acts.*</script>", response.text)
    info = re.findall('{\"actid\".*?\"}', res[0])

    count = 0
    for sec in info:
        t_t = ""
        dict = json.loads(sec)
        pa = dict["member_count"]
        pb = dict["max_member"]

        act_url = f"https://tongqu.sjtu.edu.cn/act/{dict['actid']}"
        act_res = requests.get(act_url, headers=headers)
        if re.search(r"\\u65b0\\u65f6\\u4ee3\\u793e\\u4f1a\\u8ba4\\u77e5\\u5b9e\\u8df5", act_res.text):
            print('*', end="")
            t_t = t_t+"*"

        if dict['actid'] in done_list:
            t_t = t_t+"【OK】"+pa+'/'+pb+"   "
        elif pa == pb:
            print("【已满】"+pa+'/'+pb, end="   ")
            t_t = t_t+"【已满】"+pa+'/'+pb+"   "
        elif dict["time_status"] == 2:
            t_t = t_t+"【未开】"+pa+'/'+pb+"   "
        else:
            print("【OK】"+pa+'/'+pb, end="   ")
            t_t = t_t+"【-->】"+pa+'/'+pb+"   "
        for j in ["name", "location", "start_time", "end_time"]:
            print(dict[j], end=" ")
            t_t = t_t+dict[j]+" "
        print('')
        data_set[t_t] = dict['actid']
        count = count+1
        if count > 9:
            break

    # In[3]:

    a_length = []
    for tt in data_set:
        a_length.append(len(tt))
    max_width = max(a_length)

    # In[4]:

    window = tk.Tk()
    window.title("my program")
    window.geometry(str((max_width*12+2))+"x600")

    my_list = (data_set)
    l = tk.Listbox(window, font=("Aria", 13), width=int(max_width*6))
    l.pack()
    for tt in data_set:
        l.insert("end", tt)

    def go_to():
        value = l.get(l.curselection())
        act_id = data_set[value]
        url = "https://tongqu.sjtu.edu.cn/act/"+act_id
        webbrowser.open(url)

    preserve_url = "https://tongqu.sjtu.edu.cn/api/act/sign"

    def ease_preserve():
        value = l.get(l.curselection())
        this_id = data_set[value]

        data = ""
        data["act_id"] = this_id
        requests.post(url=preserve_url, headers=headers, data=data)

        data = ""
        data["act_id"] = this_id
        requests.post(url=preserve_url, headers=headers, data=data)

        data = ""

        data["act_id"] = this_id
        requests.post(url=preserve_url, headers=headers, data=data)

        data = ""

        data["act_id"] = this_id
        requests.post(url=preserve_url, headers=headers, data=data)

        window.destroy()
        time.sleep(0.05)
        start_whole_thing()

    def ease_quit():
        value = l.get(l.curselection())
        this_id = data_set[value]
        quit_url = "https://tongqu.sjtu.edu.cn/api/act/exitAct?id=" + \
            str(this_id)
        data = {"id": this_id}
        requests.post(url=quit_url, headers=headers, data=data)
        window.destroy()
        time.sleep(0.05)
        start_whole_thing()


    def ease_book():
        pass


    b = tk.Button(text="go!", command=go_to, width=15, height=2).pack()
    b2 = tk.Button(text="一键报名", command=ease_preserve,
                   width=15, height=2).pack()
    b3 = tk.Button(text="一键退出", command=ease_quit, width=15, height=2).pack()
    b4 = tk.Button(text="一键预约主图", command=ease_book, width=15, height=2).pack()

    label_text = tk.StringVar()
    label = tk.Label(window, textvariable=label_text, fg="red").pack()

    def auto_close():
        for i in range(30):
            label_text.set(f"距离窗口关闭还有还有{30-i}秒")
            time.sleep(1)
        window.after(10, window.destroy)

    # t=threading.Thread(target=auto_close)
    #t.daemon = True
    # t.start()
    window.after(30000, window.destroy)

    window.mainloop()


# In[ ]:
if __name__ == "__main__":
    start_whole_thing()


# In[ ]:
