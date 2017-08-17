class QB:

    def is_valid(self, n):
        if n > 2.375:
            n=2.375
        elif n<0:
            n=0
        return n

    def passer_rating(self, att, yds, comp, td, ints):
        a = ((float(comp) / att)-.3)*5
        a = self.is_valid(a)
        b = ((float(yds)/att)-3)*.25
        b = self.is_valid(b)
        c = (float(td)/att)*20
        c = self.is_valid(c)
        d = 2.375-((float(ints)/att)*25)
        d = self.is_valid(d)
        #print('a',a,'b',b,'c',c,'d',d)
        return round((((a+b+c+d)/6)*100), 1)
