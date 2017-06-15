import vk
import datetime
import time

def count_tag(tag, start, end):
    st = datetime.datetime.strptime(start, "%d/%m/%y %H:%M")
    et = datetime.datetime.strptime(end, "%d/%m/%y %H:%M")
    st = time.mktime(st.timetuple())
    et = time.mktime(et.timetuple())
    session = vk.Session(access_token='a359076165df90c2e8eb0525e236fe5b38eaffd7fea441ff43a335b2e5d3d9692cf67ca30305bcd94df30')
    vk_api = vk.API(session)
    query = vk_api.newsfeed.search(q=tag,start_time=st,end_time=et)
    return(query[0], start, end)
