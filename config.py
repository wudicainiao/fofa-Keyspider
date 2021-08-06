# coding:utf-8
import time

class define:
    GREEN       = "\033[32m"
    RED         = "\033[0;31m"
    BLUE        = "\033[94m"
    ORANGE      = "\033[33m"
    Timeout     = 500
    filename    = 'out\\%s.xlsx' % time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))

    FOFA_EMAIL = ''
    Apikey = '' # 使用时替换此处Apikey

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
        Supporting CIDR format!

        python3 fofa.py [options]

    Options:
        -i  ip        eg : python3 fofa-Keyspider.py -i 8.8.8.8 8.8.8.0/24 8.8.8.8/16
        -f  ip_file   eg : python3 fofa-Keyspider.py -f 1.txt
        -k  keyword   eg : python3 fofa-Keyspider.py -k app="Solr"
    '''

