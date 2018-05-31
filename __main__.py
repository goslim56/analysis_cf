import urllib
import collection


def proc_nene(xml):
    pass


def store_nene(data):
    pass


if __name__ == '__main__':

    # nene collection
    collection.crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
            % (urllib.parse.quote('전체'), urllib.parse.quote('전체')) ,
        proc=proc_nene,
        store=store_nene)
