from gensim.models import Word2Vec

# ข้อมูลข้อความตัวอย่าง (อาจจะเป็นชุดข้อมูลที่ใหญ่กว่า)
sentences = [['dog', 'barks'], ['cat', 'meows'], ['dog', 'chases', 'cat']]

# สร้างโมเดล Word2Vec
model = Word2Vec(sentences, vector_size=10, window=2, min_count=1)

# รับเวกเตอร์ของคำ
vector = model.wv['dog']
print(vector)

# ค้นหาคำที่คล้ายกับ 'dog'
similar_words = model.wv.most_similar('dog', topn=3)
print(similar_words)
