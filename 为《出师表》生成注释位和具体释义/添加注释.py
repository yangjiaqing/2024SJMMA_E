import csv  
  
#classical_chinese = input("输入出师表文言文：").replace('\n', ' ')  
# 假设已经有了输入，为了示例，这里直接给出文本  
classical_chinese ="""
先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也。
宫中府中，俱为一体，陟罚臧否，不宜异同。若有作奸犯科及为忠善者，宜付有司论其刑赏，以昭陛下平明之理，不宜偏私，使内外异法也。
侍中、侍郎郭攸之、费祎、董允等，此皆良实，志虑忠纯，是以先帝简拔以遗陛下。愚以为宫中之事，事无大小，悉以咨之，然后施行，必能裨补阙漏，有所广益。
将军向宠，性行淑均，晓畅军事，试用于昔日，先帝称之曰能，是以众议举宠为督。愚以为营中之事，悉以咨之，必能使行阵和睦，优劣得所。
亲贤臣，远小人，此先汉所以兴隆也；亲小人，远贤臣，此后汉所以倾颓也。先帝在时，每与臣论此事，未尝不叹息痛恨于桓、灵也。侍中、尚书、长史、参军，此悉贞良死节之臣，愿陛下亲之信之，则汉室之隆，可计日而待也。
臣本布衣，躬耕于南阳，苟全性命于乱世，不求闻达于诸侯。先帝不以臣卑鄙，猥自枉屈，三顾臣于草庐之中，咨臣以当世之事，由是感激，遂许先帝以驱驰。后值倾覆，受任于败军之际，奉命于危难之间，尔来二十有一年矣。
先帝知臣谨慎，故临崩寄臣以大事也。受命以来，夙夜忧叹，恐托付不效，以伤先帝之明，故五月渡泸，深入不毛。今南方已定，兵甲已足，当奖率三军，北定中原，庶竭驽钝，攘除奸凶，兴复汉室，还于旧都。此臣所以报先帝而忠陛下之职分也。至于斟酌损益，进尽忠言，则攸之、祎、允之任也。
愿陛下托臣以讨贼兴复之效，不效，则治臣之罪，以告先帝之灵。若无兴德之言，则责攸之、祎、允等之慢，以彰其咎；陛下亦宜自谋，以咨诹善道，察纳雅言，深追先帝遗诏，臣不胜受恩感激。
今当远离，临表涕零，不知所言。
先帝深虑汉、贼不两立，王业不偏安，故托臣以讨贼也。以先帝之明，量臣之才，固知臣伐贼，才弱敌强也。然不伐贼，王业亦亡。惟坐而待亡，孰与伐之？是故托臣而弗疑也。臣受命之日，寝不安席，食不甘味。思惟北征。宜先入南。故五月渡泸，深入不毛，并日而食；臣非不自惜也，顾王业不可得偏安于蜀都，故冒危难，以奉先帝之遗意也，而议者谓为非计。今贼适疲于西，又务于东，兵法乘劳，此进趋之时也。谨陈其事如左：
高帝明并日月，谋臣渊深，然涉险被创，危然后安。今陛下未及高帝，谋臣不如良、平，而欲以长策取胜，坐定天下，此臣之未解一也。
刘繇、王朗各据州郡，论安言计，动引圣人，群疑满腹，众难塞胸，今岁不战，明年不征，使孙策坐大，遂并江东，此臣之未解二也。
曹操智计，殊绝于人，其用兵也，仿佛孙、吴，然困于南阳，险于乌巢，危于祁连，逼于黎阳，几败北山，殆死潼关，然后伪定一时耳。况臣才弱，而欲以不危而定之，此臣之未解三也。曹操五攻昌霸不下，四越巢湖不成，任用李服而李服图之，委任夏侯而夏侯败亡，先帝每称操为能，犹有此失，况臣驽下，何能必胜？此臣之未解四也。
自臣到汉中，中间期年耳，然丧赵云、阳群、马玉、阎芝、丁立、白寿、刘郃、邓铜等及曲长、屯将七十余人，突将、无前、賨叟、青羌、散骑、武骑一千余人。此皆数十年之内所纠合四方之精锐，非一州之所有；若复数年，则损三分之二也，当何以图敌？此臣之未解五也。
今民穷兵疲，而事不可息；事不可息，则住与行劳费正等。而不及今图之，欲以一州之地，与贼持久，此臣之未解六也。
夫难平者，事也。昔先帝败军于楚，当此时，曹操拊手，谓天下以定。然后先帝东连吴越，西取巴蜀，举兵北征，夏侯授首，此操之失计，而汉事将成也。然后吴更违盟，关羽毁败，秭归蹉跌，曹丕称帝。凡事如是，难可逆见。臣鞠躬尽瘁，死而后已。至于成败利钝，非臣之明所能逆睹也。
"""
print(classical_chinese)  
# 读取CSV文件中的注释  
comments = {}  
# 假设'注释.csv'文件存在，并且有两列：'名称'和'注释'  
with open('注释.csv', encoding='utf-8') as csvfile:  
    reader = csv.DictReader(csvfile)  
    for row in reader:  
        comments[row['名称']] = row['注释']  
  
# 添加脚注的函数，使用最大匹配算法，并避免重复标注  
def insert_footnotes(text, comments_dict):  
    footnote_counter = 1  
    footnotes = {}  
    footnoted_words = set()  # 用于跟踪已经标注过的词汇  
    result_text = ""  
    words = text  
    while words:  
        matched = False  
        for length in range(len(words), 0, -1):  
            word = words[0:length]  
            if word in comments_dict and word not in footnoted_words:  
                result_text += f"{word}[{footnote_counter}]"  
                footnotes[footnote_counter] = (word, comments_dict[word])  
                footnote_counter += 1  
                footnoted_words.add(word)  # 将词汇添加到已标注集合中  
                words = words[length:]  
                matched = True  
                break  
        if not matched:  
            result_text += words[0]  
            words = words[1:]  
        if words:  
            result_text += ' '  
    return result_text.strip(), footnotes  
  
# 调用函数添加脚注  
annotated_text, footnote_dict = insert_footnotes(classical_chinese, comments)  
  
# 输出添加脚注后的文言文  
print("添加脚注后的正文>>>:")  
print(annotated_text)  
  
# 输出引用的注释  
print("\n引用的注释:")  
for footnote_number, (word, comment) in sorted(footnote_dict.items()):  
    print(f"[{footnote_number}]: {word} - {comment}")
