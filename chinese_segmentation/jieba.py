import jieba.analyse

with open('C:\\Users\\chenlm\\Desktop\\1.txt',encoding='utf-8') as f:
    document = f.read()
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    with open('C:\\Users\\chenlm\\Desktop\\1_segment.txt', 'w') as f2:
        f2.write(result)
f.close()
f2.close()
