from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

article_list=[]

def add_article(topic,name,rating):
	article_ob= Knowledge(
		topic=topic,
		name=name,
		rating=rating)
	article_list.append(article_ob)
	session.add(article_ob)
	session.commit()

add_article("black holes", "black hole", 9)
add_article("art", "art", 10)
add_article("climbing", "climbing", 9)


def query_all_articles():
	 Knowledges = session.query(Knowledge).all()
	 return Knowledges

#print(query_all_articles())


def query_article_by_topic(topic):
	Topics= session.query(Knowledge).filter_by(topic=topic).first()
	return Topics
#print(query_article_by_topic("art"))


def query_article_by_rating():
	rat=input("rating")
	for i in article_list:
		if(i.rating<int(rat)):
			rates= session.query(Knowledge).filter_by(rating=rat).first()
	return rates
print(query_article_by_rating())

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
