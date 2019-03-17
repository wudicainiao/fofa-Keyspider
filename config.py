# coding:utf-8
import time

class define:
    GREEN       = "\033[32m"
    RED         = "\033[0;31m"
    BLUE        = "\033[94m"
    ORANGE      = "\033[33m"
    Timeout     = 200
    filename    = 'out/%s.txt' % time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))

    session = '***' # 使用时替换此处session
    headers = {
    'Host': 'fofa.so',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
    'X-CSRF-Token': 'cL3CBckKZAsQGMzcPQmgV4VPO54ExN0cvt1lXcCcxfIruDpUQS8bmhs+Mj4G8UnzvhgA5PRl0IMxu8LP6WuwJg==',
    'Upgrade-Insecure-Requests': '1',
    'referer_url':'result?qbase64=dGl0bGU9IkluZGV4IG9mIg%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_fofapro_ars_session='+session,
    }

    banner = '''

                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'

    [*] Author:dacAIniao@重明安全
    '''

    usage = '''
    Usage: 
        python3 fofa.py [options]

    Options:
        -u  url     eg : https://fofa.so/result?qbase64=dGl0bGU9IkluZGV4IG9mIg%3D%3D
    '''

