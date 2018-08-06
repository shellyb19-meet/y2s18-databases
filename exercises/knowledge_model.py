from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__= 'Knowledge'
	article_id=Column(Integer, primary_key=True)
	topic=Column(String)
	name=Column(String)
	rating=Column(Integer)

	def __repr__(self):
		if(self.rating<7):
			return ("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!")
		return("If you want to learn about: {}\n"
				"you should look at the Wikipedia article called: {}\n"
	        	"We gave this article a rating of: {}"
		   		" out of 10! \n").format(
			   		self.topic,
			    	self.name,
					self.rating)



		 

				

