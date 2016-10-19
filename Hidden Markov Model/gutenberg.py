import re, requests, os

def getBook(id):
      filePath = "./pg" + str(id) + ".txt"
      if not os.path.isfile(filePath):
          url = "http://www.gutenberg.org/cache/epub/"+str(id)+"/pg"+str(id)+".txt"
          raw = requests.get(url).text
          start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*", raw).end()
          stop = re.search(r"End of the Project Gutenberg EBook", raw).start()

          with open(filePath, "w") as output:
              output.write(raw[start:stop])

      with open(filePath, "r") as input:
          book = input.read()

      return book
