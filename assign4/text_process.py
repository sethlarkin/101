import string

######## Begin code which needs to be modified ##########

class MyDict(object):
    def __init__(self):
        self.mydict = {}
        return

    def insert(self, key, value):
        self.mydict[key] = value

    def contains(self, key):
        return key in self.mydict

    def value(self, key):
        return self.mydict[key]

    def delete(self, key):
        if key in self.mydict:
            del self.mydict[key]
        return

    def get_key_values(self):
        return self.mydict.items()

    def dump(self):
        for k in self.mydict:
            print(k, self.mydict[k])

class MySet(object):
    def __init__(self):
        self.myset = set([])
        return

    def insert(self, key):
        self.myset.add(key)
        return

    def contains(self, key):
        return key in self.myset

    def dump(self):
        for k in self.myset:
            print(k)

######## End code which needs to be modified ##########


# Store the set of stop words in a set object
stop_words_file = "stopwords.txt"
stop_words = MySet()

with open(stop_words_file) as f:
    for l in f:
        stop_words.insert(l.strip())


# Download file from https://snap.stanford.edu/data/finefoods.txt.gz
# Remember to gunzip before using
review_file = "foods.txt"

review_words = []
for i in range(5):
    review_words.append(MyDict())

with open(review_file, encoding='LATIN-1') as f:
    lines = f.readlines()
    idx = 0
    num_lines = len(lines) - 2
    while idx < num_lines:
        while not lines[idx].startswith("review/score"):
            idx = idx + 1

        # Jump through hoops to satisfy the Unicode encodings
        l = lines[idx].encode('ascii', 'ignore').decode('ascii')
        l = l.strip().split(":")[1].strip()

        # Extract rating
        rating = int(float(l))
        while not lines[idx].startswith("review/text"):
            idx = idx + 1

        l = lines[idx].encode('ascii', 'ignore').decode('ascii').strip().lower()
        text = l.split(":")[1].strip()
        text = text.translate(str.maketrans("","", string.punctuation))

        # Extract words in the text
        words = text.split(" ")
        # words = [x.strip(string.punctuation) for x in text.split(" ")]
        for w in words:
            if len(w) and not stop_words.contains(w):
                if review_words[rating - 1].contains(w):
                    count = review_words[rating - 1].value(w) + 1
                else:
                    count = 1
                review_words[rating - 1].insert(w, count)

# Print out the top words for each of the five ratings
for i in range(5):
    freq_words = sorted(review_words[i].get_key_values(), key=lambda tup: tup[1], reverse=True)
    print(i+1, freq_words[0:20])
