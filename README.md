# **wallet_app**
## **Table Of Content**
* [Introduction](#Introduction)
* [ SetUp](#Setup)
* [ End-points](#END-POINTS)
* [Features](#Features)

### Setup
1. Ensure Python 3.x install on your system
2. Create an account with git.
3. From your terminal/command prompt clone the repository using this git command
   * git clone <https://github.com/OgungbeniOpeoluwa/wallet_app.git>.
4. install postman to test the application end-points by providing the necessary url and body requests if necessary.



### Introduction
fastWallet is a user-friendly e-wallet application designed to 
simplify financial management. This application is build on django rest
framework and paystack. 

#### Features
* [Register](#Register)
* [Login](#Login)
* [Fund Wallet](#FundWallet)
* [Transfer](#Transfer)
* [Balance](#GetWalletBalance)
* [Transaction](#AllTransactionHistory)

### **_END-POINTS_**

#### **Register**
_This api create a new user.it takes username,email,phone number and the password.
The phone number,email,wallet pin(length 4) and password(min=8,max=16) must be valid to avoid invalid details.__

#### **Request**
* _url :_ https://wallet-app-24ay.onrender.com/user/register/
* _Method_ : POST
* Header:
       
    content-type: application/json
* Body:

    ```
  {
    'username':"username",
    'email':"user@gmail.com
    "password":"password"
    "wallet_pin":"****"
    }
  ```
  
##### _Fields_
1. username: The user preferred nick_name 
2. email: The user valid email
3. password: The user password
4. wallet_pin:The user wallet pin(required)

#### _Response 1_
##### _Successful Response_
* _status : OK 200_

* _body:_
    
  ```
  {
    "email":user@gmail.com,
    "username":"username
    }
  ```
#### Response 2
##### **_UnSuccessful Response_**
__* status: bad_request 400__

_*  body:_
        
```
        {
    "username": [
        "A user with that username already exists."
    ],
    "email": [
        "user with this email already exists."
    ]
}
```

#### Response 3
##### **_UnSuccessful Response_**
__* status: bad_request 400__

_*  body:_

```{
    "password": [
        "Ensure this field has at least 8 characters."
    ]
}


```

### **Login**

*This endpoint allows users to access the application
by providing their username and password. It returns both an access token and 
a refresh token in the response.* 

#### **Request**
* url: https://wallet-app-24ay.onrender.com/user/login/
* Method:POST
* Body:
     
 ```
   {
    "username":"ope37",
    "password":"ope1234@fast"
    }
    
   ```

##### Fields
* username:(required)
* password:(required)

##### **Response 1**
##### _Successful Response_

_* status_ : 200 OK
_*  body_ : 
   ```  
    {
    "refresh" : IsInVzZXJfF6bV_ZjKO_vCA.*****",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.*****"

    }
```

##### **Response 2**

##### **Unsuccessful  Response** 

#### * status: 400 Bad Request

##### * Body
```
{
    "Invalid credential"
}
  
```

### Fund_Wallet
_This end-point allow user to fund their wallet with ease.
it takes the amount  and return the link to make payment._

#### **Request**
* url : https://wallet-app-24ay.onrender.com/wallet/funds/
* Method: POST
* Body: 
   ``` 
  {
    "amount" :2000
    }
  ```
  
##### **Successful Response**

##### Response

* status : 200 OK
* Body:
 
   ``` 
  {
    https://checkout.paystack.com/1sjmqptmcqxhbdb
    }
  ```
  
#### **Unsuccessful Response:**
##### Response 1
* status : 400 Bad Request
* Body: 
   
  ```
  {
    "Message":"amount too low"
   }
  ```
### **Transfer**
_This end-points allow user to send money to various account
of their choice._

##### **Request**
* url: https://wallet-app-24ay.onrender.com/wallet/transfer/
* Method: POST
* Body:

   ```{
    "account_number":2037126548,
    "bank_name":"Kuda Bank",
     "amount":100,
    "wallet_pin":"***",
    "description":"feeding"
   }
  ```

##### **Fields**
* account_number: Recipient Account Number(required)
* bank_name: Recipient Bank name(required)
* wallet_pin: User wallet pin(required)
* description:  Money description(required)

##### **Unsuccessful Response**
##### **Response 1**

_* status: 400  Bad Request_
_* Body:_ 
   
```    
      {
        "message": "Insufficient funds"
       }  
```

_Response 2_

* _status : 400 Bad Request_
* _Body :_

  ```
  {
      "message": "Invalid Pin"
  }
  ```
  
##### **Successful Response**
_* status: 200 OK_

_* Body:_


```
{
    "amount": 50,
    "description": "feeding",
    "reference": "f0d1a272-82fd-47ad-abf3-a8e5227b6514",
    "paymentStatus": "pending",
    "paymentType": "transfer",
    "date_created": "2024-04-26T18:48:57.799684Z"
}
```


### **All_Transaction_History**
This end-point returns all user transaction histories.

##### **Request**
_* uri:_ https://wallet-app-24ay.onrender.com/wallet/transactions/ 

__* Method :__ GET

##### _**Successful Response**_

_* status : 200 OK_

_* Body:_

```[
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "6523h9wyrd",
        "paymentStatus": "pending",
        "paymentType": "deposit",
        "date_created": "2024-04-26T09:10:22.579343Z"
    },
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "zq4wnad3c8",
        "paymentStatus": "pending",
        "paymentType": "deposit",
        "date_created": "2024-04-26T09:30:30.601930Z"
    },
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "hpjfql5obm",
        "paymentStatus": "pending",
        "paymentType": "deposit",
        "date_created": "2024-04-26T18:31:53.399579Z"
    },
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "9v5vkqvxex",
        "paymentStatus": "pending",
        "paymentType": "deposit",
        "date_created": "2024-04-26T18:35:50.525635Z"
    },
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "3b97dykv68",
        "paymentStatus": "pending",
        "paymentType": "deposit",
        "date_created": "2024-04-26T18:39:32.702561Z"
    },
    {
        "amount": 200,
        "description": "Deposit",
        "reference": "gya7vlbfdf",
        "paymentStatus": "successful",
        "paymentType": "deposit",
        "date_created": "2024-04-26T18:44:52.482805Z"
    },
    {
        "amount": 50,
        "description": "feeding",
        "reference": "f0d1a272-82fd-47ad-abf3-a8e5227b6514",
        "paymentStatus": "pending",
        "paymentType": "transfer",
        "date_created": "2024-04-26T18:48:57.799684Z"
    }
]
```


### _**Get_Wallet_Balance**_
_This end-point return user current balance state._

Request:

* url : https://wallet-app-24ay.onrender.com/wallet/balance/

* Method: GET

#### _Successful Response_
* status: 200 OK

_* Body_:
   ``` 
   {
        "balance": 20000.0
    }
   ```⌢眠污敬⵴灡≰ഠ�