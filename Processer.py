import datetime, json

class Processer:
   def __init__(self):
      self.initialized = "> Processer initialized"
      self.empty = ""
      self.files = []
      self.participants = []
      print(f""+str(self.initialized)+"\n"+self.empty.join(["=" for i in range(len(list(self.initialized))+1)]))

   def set_files(self, files):
      self.files = files
      print(f"> Processer got {len(self.files)} files: {[str(file) for file in self.files]}") if len(self.files)>1 else print(f"> Processer got {len(self.files)} file: {[str(file) for file in self.files]}")

   def set_participants(self):
      for file in self.files:
         with open("./data/"+file, 'r') as f:
            try:
               buffer = json.load(f)['participants']
               for item in buffer:
                  self.participants.append(item['name'])
            except KeyError:
               print(f" [ERR_REPORT] - Error: {file} is not a valid json file")

   # i want to transform timestamp to date
   def get_date(self, timestamp):
      return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')