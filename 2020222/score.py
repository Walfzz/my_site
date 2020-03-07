class Student:
    def __init__(self, name, math, chi, eng, bio):
        self.name = name
        self.math = math
        self.chinese = chi
        self.english = eng
        self.biology = bio
    def info(self):
        return '{:<10}{:<10}{:<10}{:<10}{:<10}'.format(self.name, self.math, self.chinese, self.english, self.biology)

def get_math_avg(sts):
    return sum([st.math for st in sts]) / len(sts)
def get_chi_avg(sts):
    return sum([st.chinese for st in sts]) / len(sts)
def get_eng_avg(sts):
    return sum([st.english for st in sts]) / len(sts)
def get_bio_avg(sts):
    return sum([st.biology for st in sts]) / len(sts)

def pr_sts(sts):
    for st in sts:
        print(st.info())

def select_math_larger(sts, score):
    chosen = []
    for st in sts:
        if st.math > score:
            chosen.append(st)
    return chosen

def select_chinese_less(sts, score):
    chosen = []
    for st in sts:
        if st.chinese > score:
            chosen.append(st)
    return chosen

def select_biology_higher_avg(sts):
    chosen = []
    for st in sts:
        if st.biology > get_bio_avg(sts):
            chosen.append(st)
    return chosen

def selct_english_lowest(sts):
    with open('students.txt') as f:
        for line in f:
            ts = line.strip().split()
            eng = float(ts[3])
            chosen = []
            for st in sts:
                if st.english < eng:
                    chosen.append(st)
            return chosen

def read_scores():
    with open('students.txt') as f:
        line = f.readline()
        print(line)
        sts = []
        for line in f:
            ts = line.strip().split()
            #print(ts)
            name = ts[0]
            math = float(ts[1])
            chi = float(ts[2])
            eng = float(ts[3])
            bio = float(ts[4])
            st = Student(name, math, chi, eng, bio)
            sts.append(st)
            print(st.info())
        
    math_avg = get_math_avg(sts)
    chi_avg = get_chi_avg(sts)
    eng_avg = get_eng_avg(sts)
    bio_avg = get_bio_avg(sts)
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    print(fmt.format('avg:', math_avg, chi_avg, eng_avg, bio_avg))
    print('-'* 50)
    lst1 = select_math_larger(sts, 70)
    pr_sts(lst1)
    print('-'*50)
    lst2 = select_chinese_less(sts, 70)
    pr_sts(lst2)
    print('-'*50)
    lst3 = select_biology_higher_avg(sts)
    pr_sts(lst3)
    print('-'*50)
    lst4 = selct_english_lowest(sts)
    pr_sts(lst4)

read_scores()
