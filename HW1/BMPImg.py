import struct
HEADER_NUM = 15;
HEADER_SIZE = [2,4,4,4,4,4,4,2,2,4,4,4,4,4,4];
HEADER_INFO = ["Identifier","FileSize","Reserved","BitmapDataOffset",
               "BitmapHeaderSize","Width","Height","Planes",
               "BitsPerPixel","Compression","BitmapDataSize","H_Resolution",
               "V_Resolution","UsedColors","ImportantColors"];

class BMPHead:
    def __init__(self):
        self.Identifier = '';
        self.FileSize = 0;
        self.Reserved = 0;
        self.BitmapDataOffset = 0;
        self.BitmapHeaderSize = 0;
        self.Width = 0;
        self.Height = 0;
        self.Planes = 0;
        self.BitsPerPixel = 0;
        self.Compression = 0;
        self.BitmapDataSize = 0;
        self.H_Resolution = 0;
        self.V_Resolution = 0;
        self.UsedColors = 0;
        self.ImportantColors = 0;

    def setValue(self,i,a):
        if i==0:
            self.Identifier = a
        elif i==1:
            self.FileSize = a
        elif i==2:
            self.Reserved = a
        elif i==3:
            self.BitmapDataOffset = a
        elif i==4:
            self.BitmapHeaderSize = a
        elif i==5:
            self.Width = a
        elif i==6:
            self.Height = a
        elif i==7:
            self.Planes = a
        elif i==8:
            self.BitsPerPixel = a
        elif i==9:
            self.Compression = a
        elif i==10:
            self.BitmapDataSize = a
        elif i==11:
            self.H_Resolution = a
        elif i==12:
            self.V_Resolution = a
        elif i==13:
            self.UsedColors = a
        elif i==14:
            self.ImportantColors = a
    def getWidth(self):
        return int.from_bytes(self.Width,byteorder='little')
    def getHeight(self):
        return int.from_bytes(self.Height,byteorder='little')
    def getBitsPerPixel(self):
        return int.from_bytes(self.BitsPerPixel,byteorder='little')
    def updateGetDict(self):
        #我後來直接把這個的功能放到rotate,filter裡面 比較好

        return
class BMPImg:
    def __init__(self):
        self.header = BMPHead();
        self.data = "";
    
    def loadPic(self, picPath):
        pic = open(picPath, 'rb');
        
        for i in range(HEADER_NUM):
            a = pic.read(HEADER_SIZE[i]);
            self.header.setValue(i, a);
    
        dataSize = self.getPxlNum() * self.getBytesPerPixel();
        self.data = pic.read(int(dataSize));

        pic.close();
            
    def getWidth(self):
        return self.header.getWidth();
    
    def getHeight(self):
        return self.header.getHeight();
    
    def getPxlNum(self):
        return self.header.getWidth() * self.header.getHeight();
    
    def getBytesPerPixel(self):
        return self.header.getBitsPerPixel() / 8;
    
    def printHeader(self):
        getDict = {
            "Identifier": self.header.Identifier,
            "FileSize": self.header.FileSize,
            "Reserved": self.header.Reserved,
            "BitmapDataOffset": self.header.BitmapDataOffset,
            "BitmapHeaderSize": self.header.BitmapHeaderSize,
            "Width": self.header.Width,
            "Height": self.header.Height,
            "Planes": self.header.Planes,
            "BitsPerPixel": self.header.BitsPerPixel,
            "Compression": self.header.Compression,
            "BitmapDataSize": self.header.BitmapDataSize,
            "H_Resolution": self.header.H_Resolution,
            "V_Resolution": self.header.V_Resolution,
            "UsedColors": self.header.UsedColors,
            "ImportantColors": self.header.ImportantColors
        }
        
        for h in HEADER_INFO:
            print(h+":", getDict[h]);

    def storePic(self, outputPath):
        
        #self.header.updateGetDict();
        getDict = {
            "Identifier": self.header.Identifier,
            "FileSize": self.header.FileSize,
            "Reserved": self.header.Reserved,
            "BitmapDataOffset": self.header.BitmapDataOffset,
            "BitmapHeaderSize": self.header.BitmapHeaderSize,
            "Width": self.header.Width,
            "Height": self.header.Height,
            "Planes": self.header.Planes,
            "BitsPerPixel": self.header.BitsPerPixel,
            "Compression": self.header.Compression,
            "BitmapDataSize": self.header.BitmapDataSize,
            "H_Resolution": self.header.H_Resolution,
            "V_Resolution": self.header.V_Resolution,
            "UsedColors": self.header.UsedColors,
            "ImportantColors": self.header.ImportantColors
        }
        pic = open(outputPath, 'wb');
        for h in HEADER_INFO:
            pic.write(getDict[h]);
        for e in self.buf:
            pic.write(e);
        pic.close();
        print("--- Store Picture ---")
        
    def rotate(self):
        print("--- rotate ---")
        self.buf = list()
        for e in self.data:
            self.buf.append(bytes([0]))
        w=self.getWidth()
        h=self.getHeight()

        #count算橫向的掃描每個點
        #shift是完成幾次的橫向
        count=0
        shift=1
        k=0
        for i in range(len(self.data)):
            #原圖:左下->右下的儲存,轉90度:右下->右上的進行
            self.buf[(count*h)*3+(h-shift)*3+k]=bytes([self.data[i]])
            k+=1
            if k==3:
                k=0
                count+=1
            #掃完一個橫排,shift+1
            if count == w:
                count=0
                shift+=1

        #改圖片的header, 因為是轉90度所以長寬互換
        temp=self.header.Width
        self.header.Width=self.header.Height
        self.header.Height=temp
        #initialize
        #TODO
        
    def RGB2Y(self):
        print("--- RGB to Y ---")
        #TODO
        #存byte資料用的
        self.buf=list()
        for i in range(len(self.data)):
            if i%3==0:
                Y = int(0.3*self.data[i] + 0.59*self.data[i+1] + 0.11*self.data[i+2])
                #存RGB值,(R=G=B) 所以同個存3次
                self.buf.append(bytes([Y]))
                self.buf.append(bytes([Y]))
                self.buf.append(bytes([Y]))

    def PrewittFilter(self):
        
        #Convert image to grayscale
        self.RGB2Y();
        print("--- PrewittFilter ---")
        #TODO: bonus
        w=self.getWidth()
        h=self.getHeight()
        #存byte資料用的
        self.secondbuf=self.buf
        self.buf=list()
        #count算橫向的pixel
        count=1
        for i in range(len(self.secondbuf)):
            #RGB3點一pixel
            if i%3==0:
                #邊界條件,如果超出右邊的邊界1,2格,則補黑點
                if count>w:
                    if ((count+2)%w==1 or (count+2)%w==2):
                        count+=1
                        self.buf.append(bytes([0]))
                        self.buf.append(bytes([0]))
                        self.buf.append(bytes([0]))
                        continue
                try:
                    #我設起始點為x7(filter左下)
                    x7=int.from_bytes(self.secondbuf[i],byteorder='little')
                    x8=int.from_bytes(self.secondbuf[i+3],byteorder='little')
                    x9=int.from_bytes(self.secondbuf[i+6],byteorder='little')
                    x4=int.from_bytes(self.secondbuf[i+w*1*3],byteorder='little')
                    x5=int.from_bytes(self.secondbuf[i+w*1*3+3],byteorder='little')
                    x6=int.from_bytes(self.secondbuf[i+w*1*3+6],byteorder='little')
                    x1=int.from_bytes(self.secondbuf[i+w*2*3],byteorder='little')
                    x2=int.from_bytes(self.secondbuf[i+w*2*3+3],byteorder='little')
                    x3=int.from_bytes(self.secondbuf[i+w*2*3+6],byteorder='little')

                    Gx=-x1-x4-x7+x3+x6+x9
                    Gy=-x1-x2-x3+x7+x8+x9
                    G=int((Gx**2+Gy**2)**0.5)
                    if G>255:
                        G=255
                    #以G數set 1 pixel的點(R=G=B)
                    self.buf.append(bytes([G]))
                    self.buf.append(bytes([G]))
                    self.buf.append(bytes([G]))
                except:
                    #超出上界,補黑點
                    self.buf.append(bytes([0]))
                    self.buf.append(bytes([0]))
                    self.buf.append(bytes([0]))
                count+=1

        #這裡可改圖片header中的長寬
        #原本是要改成w-2,h-2, 但作業要求中說
        #"Tomake this homework simple, you won’t change the dimensions"
        #我就維持不變,減少的兩行補全黑的點(我猜是這個意思)
        self.header.Width=struct.pack("<I", w)
        self.header.Height=struct.pack("<I", h)