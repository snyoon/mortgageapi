## Mortgage Calculator REST api
### Set Up.
After checking out the repository head to the top level directory and start a virtual environment. 

	   $ virtualenv venv
In the venv install the dependencies stored in the requirements.txt file

	    $ pip install requirements.txt

This REST api also uses [Redis](https://redis.io/topics/introduction) to handle the caching required to session storage. 
For development/demo use you can start your own Redis server by using their [windows client](https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/) or on mac their [cli](https://redis.io/topics/quickstart).

Once you have the redis server up use the 

		$ flask run
command to start the web api.

### How to Use
Replace the {} in the following calls with the correct information. 

**/payment-amount [GET]**
*dev-server-url-here* **/payment-amount?askingprice={}&downpayment={}&schedule={}&period={}**
Use this api call to find the recurring payment amount of a mortgage with a specific asking price, down payment*, payment schedule**, amortization period***. The rate of the mortgage will be the one you prespecified or the default 2.5%

**/mortgage-amount [GET]**
*dev-server-url-here* **/mortgage-amount?paymentamount={}&schedule={}&period={}**
Use this api call to find the total amount of a mortgage and mortgage insurance with a recurring payment value, payment schedule**, amortization period***. The rate of the mortgage will be the one you prespecified or the default 2.5%

**/interest-rate [PATCH]**
*dev-server-url-here* **/interest-rate**
**Request body:**

    {'Interest Rate' : XXX}
   Use this api call to change the interest rate you are dealing with. This rate carries on over till the end of the session. 
  
**Formats:**

 - askingprice : 500000
 - downpayment : 100000
 - schedule : monthly
 - period : 15
 - Interest Rate request body should be a json object labeled interest rate with a number in percentage form i.e 10 for 10%






*Must be at least 5% of first $500k plus 10% of any amount above $500k (So $50k on a $750k
mortgage)


** Min 5 years, max 25 years


*** Weekly, biweekly, monthly
