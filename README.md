This is API for POST test  based on PYTHON and FastAPI framework. 
The reason of choosing FastAPI instead of Django or flask is better performance of ASYNC functions. 
By the way we can create more simple api with flask or Django by using asyncio and uvicorn library and wrap up all the async functions with (asycn- await) but the performance and documentation of FastAPI is much better that the others. 


#Routs:
What is this API for.
This API will create a note in PostgrSQL daba base. 
This API contains 3 routs:
http://localhost:8002/docs
	in this rout you can see all the documents and even you can test the api 
  
http://localhost:8002/response
by calling this rout you can see a simple response that shows this API is up and we can communicate with. 

http://localhost:8002/notes/
	this end point will receive a JSON in this format: 
		{
			“title”: “string”;
			“description”: ”string”
		}
	For test this function you can send a post request with post man to this rout and get back a JSON response to show you the title and description and id of that note



#Running up the project ( COMPOSE UP ) : 
First you need to download and install docker on you machine.
Then you just need to execute below command :
docker-compose up -d –build

you can shut down the container with the below command: 
docker-compose down 


#TESTING: 
In this project we have test cases too. For testing you just need to run  the project and then run this command : 
docker-compose exec web pytest .

