from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_article(topic,name,rating):
	article_ob= Knowledge(
		topic=topic,
		name=name,
		rating=rating)
	session.add(article_ob)
	session.commit()

add_article("black holes", "black hole", 9)
add_article("art", "art", 10)
add_article("climbing", "climbing", 10)


def query_all_articles():
	 Knowledges = session.query(Knowledge).all()
	 return Knowledges

#print(query_all_articles())


def query_article_by_topic(topic):
	Topics= session.query(Knowledge).filter_by(topic=topic).first()
	return Topics
#print(query_article_by_topic("art"))


def query_article_by_rating(rat):
	rates= session.query(Knowledge).filter(Knowledge.rating<rat).all()
	return rates
#print(query_article_by_rating(10))

def query_article_by_primary_key(idd):
	ids=session.query(Knowledge).filter_by(article_id=idd).first()
	return ids
#print(query_article_by_primary_key(1))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()
#delete_article_by_topic("art")
#print(query_all_articles())
	

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
#delete_all_articles()
#print(query_all_articles())

def edit_article_rating(name,update_rating):
	article_ob=session.query(Knowledge).filter_by(name=name).first()
	article_ob.rating=update_rating
	session.commit()
#edit_article_rating("art",7)
#print(query_all_articles())

def delete_article_by_rating(rat):
	knowledge=query_article_by_rating(rat)
	for i in knowledge:
		session.query(Knowledge).filter_by(article_id=i.article_id).delete()
	session.commit()
#delete_article_by_rating(10)
print(query_all_articles())

def top_2():
	top_rat=10
	a=-1
	top=[]
	stop=True
	knowledge=query_all_articles()
	while(stop):
		for i in knowledge:
			if(i.rating==top_rat):
				top.append(i)
				a=a+1
				if(a==1):
					stop=False
		top_rat=top_rat-1
	return top

#print(top_2())
def edi_article_rating(name,update_rating):
	article_ob=session.query(Knowledge).filter_by(name=name).first()
	article_ob.rating=((update_rating+article_ob.rating)/2)
	session.commit()
edi_article_rating("art",6)
print(query_all_articles())

