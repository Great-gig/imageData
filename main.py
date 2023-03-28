import pickle
from PIL import Image


class object:
    def __init__(self, seed):
        self.length = len(str(seed))
        self.even = not seed % 2
        self.id = seed
        self.longstring = """
        What is Lorem Ipsum?
        
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
        standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a 
        type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
        Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
        Ipsum. Why do we use it? 
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
        standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a 
        type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
        Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
        Ipsum. Why do we use it? 
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
        standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a 
        type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
        Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
        Ipsum. Why do we use it?  """
        self.floatArray = [0.0123123123, 1231.23123, -123123132.123123]

    def __str__(self):
        output = f"This object has a character length of {self.length} and "
        if self.even:
            output += "is even."
        else:
            output += "is odd."
        output += f"\n my long string is {len(self.longstring)} long and I have {len(self.floatArray)} floats."
        return output

    def copyAttributes(self, o):
        self.length = o.length
        self.even = o.even
        self.longstring = o.longstring
        self.floatArray = o.floatArray

    def save(self, filename):
        with open(filename + '.sav', 'wb') as handle:
            pickle.dump(self, handle)

    def load(self, filename):
        with open(filename + '.sav', 'rb') as handle:
            b = pickle.load(handle)
        self.copyAttributes(o)

    def encrypt(self, filename):
        b1 = self.tobytes()
        image = Image.open('input.png')
        mode = image.mode
        h, w = image.size

        imb = image.tobytes()
        b2 = encryptbytes(b1, imb)
        outImage = Image.frombytes(mode, (h, w), b2)

        outImage.save(filename + '.png')

    def unencrypt(self, filename):
        b = Image.open(filename + '.png').tobytes()
        b = unencryptbytes(b)
        self.frombytes(b)

    def tobytes(self):
        b = pickle.dumps(self)
        return b

    def frombytes(self, b):
        o = pickle.loads(b)
        self.copyAttributes(o)


def encryptbytes(b1, b2):
    a1 = list(b1)
    a2 = list(b2)
    a1len = len(a1)
    if a1len >= len(a2) or a1len > 255*255*255:
        print(f"encryption too big. object size: {a1len}, container size: {len(a2)}")
        return
    return bytes(to3bytes(a1len) + a1 + a2[a1len + 3:])


def unencryptbytes(b):
    a = list(b)
    alen = from3bytes(a[0:3])
    if alen > len(a) - 1:
        print("falty encryption")
        return
    return bytes(a[3:alen + 3])


def to3bytes(i):
    return [a % 255 for a in [i, i // 255, i // (255 * 255)]]

def from3bytes(i):
    return i[0]+i[1]*255+i[2]*255*255

if __name__ == '__main__':
    o = object(999)
    print(o)

    o.encrypt("output")
    o.unencrypt("output")

    print(o)
