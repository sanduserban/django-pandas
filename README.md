## Setup
1. `pip install -r requirements.txt`

2. `python manage.py migrate`

3. `python manage.py runserver`

##### CURL TESTING:
1. Ingestion example:
`curl --location --request POST 'http://127.0.0.1:8000/candidates/ingest/' \
--header 'Content-Type: application/json' \
--data-raw '[{"id":1,"first_name":"Annmarie","last_name":"Crooke","email":"acrooke0@gizmodo.com","gender":null,"date_of_birth":"09/07/1978","industry":"Other Specialty Stores","salary":180466.37,"years_of_experience":10},
{"id":2,"first_name":"Morrie","last_name":"Lahive","email":"mlahive1@imdb.com","gender":null,"date_of_birth":"20/04/1948","industry":"Diversified Financial Services","salary":239640.0,"years_of_experience":6},
{"id":3,"first_name":"Matthias","last_name":"Roden","email":"mroden2@abc.net.au","gender":"M","date_of_birth":"30/11/1998","industry":"Metal Fabrications","salary":139679.79,"years_of_experience":31},
{"id":4,"first_name":"Madelin","last_name":"Domke","email":"mdomke3@mozilla.com","gender":null,"date_of_birth":"05/05/1979","industry":"n/a","salary":196786.25,"years_of_experience":12},
{"id":5,"first_name":"Thain","last_name":"Souter","email":"tsouter4@cisco.com","gender":"M","date_of_birth":"03/08/2002","industry":"n/a","salary":140291.87,"years_of_experience":28},
{"id":6,"first_name":"Leupold","last_name":"Dignum","email":null,"gender":"M","date_of_birth":"02/08/1973","industry":"Commercial Banks","salary":30132.93,"years_of_experience":16},
{"id":7,"first_name":"Maxim","last_name":"Mackro","email":"mmackro6@goo.ne.jp","gender":null,"date_of_birth":"25/07/1929","industry":"Computer Software: Prepackaged Software","salary":89314.84,"years_of_experience":14},
{"id":8,"first_name":"Belita","last_name":"Depper","email":"bdepper7@reddit.com","gender":null,"date_of_birth":"15/11/1986","industry":"n/a","salary":null,"years_of_experience":null},
{"id":9,"first_name":"Jorry","last_name":"Kinzett","email":"jkinzett8@de.vu","gender":null,"date_of_birth":"03/11/1949","industry":"Computer Software: Prepackaged Software","salary":141421.18,"years_of_experience":4},
{"id":10,"first_name":"Steffane","last_name":"Ferrers","email":"sferrers9@ebay.com","gender":null,"date_of_birth":"03/09/1958","industry":"n/a","salary":44305.98,"years_of_experience":35},
{"id":11,"first_name":"Wendell","last_name":"Cavan","email":null,"gender":"M","date_of_birth":"11/12/1963","industry":"Mining & Quarrying of Nonmetallic Minerals (No Fuels)","salary":249309.31,"years_of_experience":10},
{"id":12,"first_name":"Monro","last_name":"Reames","email":"mreamesb@tumblr.com","gender":"M","date_of_birth":"05/04/1982","industry":"Packaged Foods","salary":124194.64,"years_of_experience":23},
{"id":13,"first_name":"Melloney","last_name":"Ambrose","email":"mambrosec@jugem.jp","gender":"F","date_of_birth":"26/08/1986","industry":"Real Estate Investment Trusts","salary":206917.89,"years_of_experience":6},
{"id":14,"first_name":"Debi","last_name":"Harrop","email":"dharropd@elegantthemes.com","gender":"F","date_of_birth":"09/03/1952","industry":"Telecommunications Equipment","salary":93330.17,"years_of_experience":14}
]'`
   
2. Average
####### Parameters:
- `group`- the field to realise the groupby on.
- `average`- the field to Average.
```
curl --location --request GET 'http://127.0.0.1:8000/candidates/average?group=industry&average=age' \
--header 'Content-Type: application/json'
```

3. For all the other REST calls just use the standard URL with the desired method: PATCH, DELETE, GET, POST
`http://127.0.0.1:8000/candidates/`