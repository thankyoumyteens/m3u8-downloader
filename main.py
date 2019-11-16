import urllib.request


# 下载视频
def saveVideo(tsUrl, fileName):
    # 当前下载的ts文件名
    tsTmp = tsUrl[tsUrl.rindex('/') + 1:]
    print('downloading ' + tsTmp)
    # get请求
    tsResponse = urllib.request.urlopen(tsUrl, data=None, timeout=10)
    tsData = tsResponse.read()

    # 打开文件, ab+: 追加byte数据
    file = open(fileName, 'ab+')
    file.write(tsData)
    file.close()


urlPrefix = 'https://leshi.iqiyi-kuyunzy.com/20190517/12233_ae099c5f/800k/hls/'
m3u8FileName = 'index.m3u8'

url = urlPrefix + m3u8FileName
# 视频文件名
videoName = 'out.ts'

# 获取m3u8文件
m3u8Response = urllib.request.urlopen(url, data=None, timeout=10)
m3u8Data = m3u8Response.read().decode()

# 读取m3u8内容
lineArray = m3u8Data.split('\n')
print('start...')
for line in lineArray:
    # 跳过注释
    if line.startswith('#'):
        continue
    saveVideo(urlPrefix + line, videoName)
print('finished...')
