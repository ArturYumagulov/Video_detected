from scaning_path_save_path import scan_yandex, yandex_upload, scan_dir, proxy_parse
from threading import Timer
import yadisk

ya = yadisk.YaDisk(id, pas, token)


lst_1 = scan_yandex(id, pas, token)
lst_2 = scan_dir("/home/zico/PycharmProjects/untitled/photo/")


arg_list = [id, pas, token, lst_2, lst_1]
t = Timer(10.0, yandex_upload, arg_list)
p = Timer(10.0, proxy_parse)
t.start()
p.start()

