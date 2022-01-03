from Processer import Processer
import datetime

# files = ['entrep.json', 'francois_gutilla.json', 'error.json']
files = ['entrep.json']

if __name__ == '__main__':
   processer = Processer()
   processer.set_files(files)
   processer.set_participants()
   # print(processer.get_date('1616688209090'.date()))