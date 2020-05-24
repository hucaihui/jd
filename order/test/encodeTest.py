import requests
from urllib import parse


if __name__=='__main__':



    #### bbb [ffff](ccccc)
    desp = '%23%23+aaa%0D%0A%23%23%23%23+bbb+%5Bffff%5D(ccccc)'


    desp="## aaa" \
         "#### bbb [ffff](ccccc)"

    print(parse.quote(desp))
