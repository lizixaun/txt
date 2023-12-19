links = soup.find_all('a', href=re.compile(r'/sing/\w+\.html'), target='_mp3')
#<a href="/sing/3bda8023f4c723e1c8537d8f58c69044.html" target="_mp3" title="晴天">…</a>
# <a href="/sing/892b7ad62499c97a1a994454423e30f6.html" target="_mp3" title="说好的幸福呢">
# <a href="/sing/16c8ab298231370293d16bcf9e5ff9b6.html" target="_mp3" title="夜曲">…</a>
